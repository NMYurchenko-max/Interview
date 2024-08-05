
### Решения по теме: Подготовка к собеседованию

- [Задание 1 и 2](https://github.com/netology-code/py-homeworks-advanced/blob/new_hw_tests/7.Interview/README.md)

- Исполнение
  * [stacl_class.py](/stack_class.py)
  * [check_balances.py](/check_balances.py)
  
- [Задание 3](https://github.com/netology-code/py-homeworks-advanced/blob/new_hw_tests/7.Interview/PEP8.md)
  
- Исполнение
  * [Папка refactoring](refactoring/)
  
    где:
  
     * [код для рефакторинга](/refactoring/script_for_refactoring.py)

     * [refactoring.py](/refactoring/refactoring.py)
  
  Кроме упорядочивания кода использованы:
  логирование ч/з декаратор логера и удаление из кода персональных данных с переносом в .env

      Для использования персональных данных:
      ```
      pip install python-dotenv
      ```
      Затем заполните файл .env в корневой директории проекта и добавив в него свои логин и пароль
      ```
      EMAIL_LOGIN=login
      EMAIL_PASSWORD=password
      ```
    ВНИМАНИЕ! Для использования почты gmail из стороннего приложения (как наше) - необхолимо вместо обычного пароля использовать Специальный пароль для приложений Googl, его получите войдя по ссылку в свой аккаунт, раздел "Пароли приложений":

    [Пароли приложений Googl](https://myaccount.google.com/apppasswords?rapt=AEjHL4OSQYe8H81yWB7ZFMQ78yh8GtNOvgDnqnwv9MSuPBORsyiphidbCzmbuRJCT8pLtvZA7EKiuLh4cpqpXJ_VbfHcSqzSTCDEjkj2b0Rn6mdh9hDbprk)

Убедитесь что у вас установлены все необходимые пакеты.
Установите необходимые пакеты для рефакторинга из файла зависимостей:
pip install -r requirements.txt
