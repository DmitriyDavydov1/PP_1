Карты и счета
Программа изменяет вид банковских карт и четов клиентов, сортирует их по дате создания и фильтрует по ключу "state". На данный момент тестируется в ручном режиме.

Описание
Зависимости
Установка и конфигурация
Начало работы
Тестирование
Deploy и CI/CD
...

Зависимости
Pyton 3.8
requests 2.32.3
flake8 3.8.1
mypy 0.4.3

Установка и конфигурация
Расположен в репозитории
git clone
https://github.com/DmitriyDavydov1/PP_1.git
установить Poetry и PyCharm.
На данный момент данные вводятся напрямую в модулях.

Использование
Проект состоит из трех модулей:
masks, widget и processing.

masks
Преобразует номер карты и номер счета и возвращает их маски в виде "XXXX XX** **** XXXX" и "**XXXX".

widget
преобразует номер карты и счета, а также преобразует дату к виду "Y-m-d H:M:S.f".

processing
фильтрует операции по ключу state и сортирует операций по дате.

Тестирование
на данном этапе не исполнено.

Deploy и CI/CD
Модули исполняются в PyCharm Community Edition 2024.1.2

FAQ
Ответы не вопросы пользователей

Проект разработан в качестве исполнения домашних заданий

Дмитрий Давыдов — Back-End Engineer
