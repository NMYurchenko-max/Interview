import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from logging_decorator import logger

# Загрузка переменных окружения из файла .env
load_dotenv()


class EmailClient:
    def __init__(self, smtp_server, imap_server, login, password):
        """
        Инициализация клиента электронной почты.
        :param smtp_server: SMTP сервер для отправки писем
        :param imap_server: IMAP сервер для получения писем
        :param login: Логин для входа в почтовый ящик
        :param password: Пароль для входа в почтовый ящик
        """
        self.smtp_server = smtp_server
        self.imap_server = imap_server
        self.login = login
        self.password = password
        self.mail = None

    @logger('my_log.log')
    def send_email(self, subject, recipients, message):
        """
        Отправка электронного письма.
        :param subject: Тема письма
        :param recipients: Список получателей
        :param message: Текст сообщения
        """
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        # Отправка письма через SMTP сервер
        with smtplib.SMTP(self.smtp_server, 587) as server:
            server.ehlo()  # Идентификация клиента
            server.starttls()  # Начало шифрования TLS
            server.ehlo()  # Повторная идентификация
            server.login(self.login, self.password)  # Вход в почтовый ящик
            server.sendmail(self.login, recipients, msg.as_string())
            # Отправка письма

    @logger('my_log.log')
    def receive_email(self, header=None):
        """
        Получение последнего электронного письма по заданному заголовку.
        :param header: Заголовок для поиск
        (по умолчанию None - получаем последнее письмо)
        :return: Объект email.message с последним полученным письмом
        """
        with imaplib.IMAP4_SSL(self.imap_server) as mail:
            mail.login(self.login, self.password)  # Вход в почтовый ящик
            mail.select("inbox")  # Выбор папки "Входящие"

            # Если заголовок указан, ищем письма с этим заголовком
            if header:
                criterion = '(HEADER Subject "%s")' % header
                result, data = mail.uid('search', None, criterion)
                if not data[0]:
                    raise Exception('Нет писем с текущим заголовком')
                latest_email_uid = data[0].split()[-1]
                # Получаем UID последнего письма с указанным заголовком
            else:
                # Если заголовок не указан, ищем только последнее письмо
                result, data = mail.uid('search', None, '(ALL)')
                if not data[0]:
                    raise Exception('Нет писем в папке "Входящие"')
                latest_email_uid = data[0].split()[-1]
                # Получаем UID последнего письма

            # Получаем последнее письмо по его UID
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            return email_message

    @logger('my_log.log')
    def display_email(self, email_message):
        """
        Вывод информации о письме.
        :param email_message: Объект email.message
        """
        print("От:", email_message['From'])
        print("Кому:", email_message['To'])
        print("Тема:", email_message['Subject'])
        print("Дата:", email_message['Date'])

        # Вывод текста письма
        if email_message.is_multipart():
            text_part_found = False
            # Флаг для отслеживания наличия текстовой части
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    if not text_part_found:  # Печатаем текст только первый раз
                        print("Текст письма:\n", part.get_payload(
                            decode=True).decode(part.get_content_charset()))
                        text_part_found = True
                        # Устанавливаем флаг в True, - не печатать текст снова
        else:
            print("Текст письма:\n", email_message.get_payload(
                decode=True).decode(email_message.get_content_charset()))


if __name__ == '__main__':
    # Пример использования
    email_client = EmailClient(
        smtp_server='smtp.gmail.com',
        imap_server='imap.gmail.com',
        login=os.getenv('EMAIL_LOGIN'),
        # Чтение логина из переменной окружения
        password=os.getenv('EMAIL_PASSWORD')
        # Чтение пароля из переменной окружения
    )

    # Отправка письма
    email_client.send_email(
        subject='Subject',
        recipients=['vasya@email.com', 'petya@email.com'],
        message='Message'
    )

    # Получение последнего письма
    received_email = email_client.receive_email()
    email_client.display_email(received_email)
    # Выводим информацию о полученном письме
