User Management System

Данный проект реализует систему управления пользователями с использованием объектно-ориентированного программирования (OOP).

Проект включает:

Класс User — хранит данные пользователя

Класс UserService — управляет пользователями

Класс UserUtil — содержит вспомогательные статические методы

Модульные тесты (pytest)


Структура проекта
week 4/
├── user.py
├── user_service.py
├── user_util.py
├── main.py
├── test_user.py
├── test_user_service.py
├── test_user_util.py
└── README.md




Перейти в папку проекта:

cd "week 4"


Запуск демонстрации:

python main.py


Запуск тестов

Установка pytest (если не установлен):

python -m pip install pytest


Запуск тестов:

python -m pytest -q


После запуска команды:
python -m pytest -q


Пример вывода:
..........                                                                 [100%]
10 passed in 0.14s