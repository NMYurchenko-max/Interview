from datetime import datetime
# from functools import wraps


def logger(log_file='my_log.log'):
    """
    Декоратор для логирования информации о вызове другой функции.
    Параметры:
    - log_file: Имя файла, в который будут записываться логи.
    Возвращает:
    - Результат вызова исходной функции.
    Логирует:
    - Временную метку момента вызова функции.
    - Имя вызываемой функции.
    - Переданные аргументы функции.
    - Значение, возвращаемое функцией.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Вызов оригинальной функции с переданными аргументами
            result = func(*args, **kwargs)
            # Получение текущего времени
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Получение имени оригинальной функции
            function_name = func.__name__
            # Преобразование аргументов в строковое представление
            args_str = ', '.join([repr(arg) for arg in args])
            # Преобразование ключевых аргументов в строковое представление
            kwargs_str = ', '.join([
                f'{key}={repr(val)}'
                for key, val in kwargs.items()
            ])
            # Комбинирование аргументов и ключевых аргументов
            all_args = ', '.join(filter(None, [args_str, kwargs_str]))
            # Преобразование результата в строковое представление
            return_value = repr(result)

            # Конструкция сообщения лога
            log_message = (
                f'{timestamp} - '
                f'{function_name}({all_args}) -> '
                f'{return_value}\n'
            )
            # Добавление сообщения лога в файл
            with open(log_file, 'a', encoding='utf-8') as log_file_obj:
                log_file_obj.write(log_message)

            # Вывод подтверждающего сообщения
            print(f'Данные записаны в файл {log_file}')

            # Возврат результата оригинальной функции
            return result

        return wrapper

    return decorator
