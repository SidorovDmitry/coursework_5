# 🎯 Habit Tracker - Трекер Привычек

## 🚀 Описание проекта
**Habit Tracker** - это RESTful API для отслеживания и управления привычками. Пользователи могут создавать, отслеживать и получать напоминания о своих привычках через Telegram.



---

## ⚡ Основные возможности

- ✅ Создание и управление привычками
- 🔔 Напоминания через Telegram бота
- 🔐 JWT аутентификация
- 📊 Пагинация и фильтрация
- 📚 Автоматическая документация API
- ⏰ Периодические задачи через Celery


---

## 🛠 Технологический стек

- **Backend**: Django 4.2+, Django REST Framework
- **База данных**: PostgreSQL
- **Аутентификация**: JWT (Simple JWT)
- **Очереди задач**: Celery + Redis
- **Документация**: DRF Spectacular (Swagger/Redoc)
- **Уведомления**: Telegram Bot API
- **CORS**: django-cors-headers

---

## 📁 Структура проекта
```commandline
coursework_5/          # Корневая директория проекта
├── 📁 config/         # Настройки Django проекта
│ ├── init.py
│ ├── settings.py # Основные настройки приложения
│ ├── urls.py           # Главный URL dispatcher
│ ├── wsgi.py           # WSGI конфигурация
│ ├── asgi.py           # ASGI конфигурация
│ └── celery.py         # Конфигурация Celery
│
├── 📁 habits/          # Приложение для управления привычками
│ ├── 📁 migrations/    # Миграции базы данных
│ │ └── init.py
│ ├── init.py
│ ├── admin.py          # Регистрация моделей в админке
│ ├── apps.py           # Конфигурация приложения Habits
│ ├── models.py         # Модели данных (Habit, Reward)
│ ├── views.py          # ViewSet'ы и API endpoints
│ ├── serializers.py    # Сериализаторы Django REST Framework
│ ├── urls.py           # URL маршруты приложения habits
│ ├── permissions.py    # Кастомные permissions
│ ├── services.py       # Бизнес-логика и сервисные функции
│ ├── tasks.py          # Celery задачи для напоминаний
│ └── tests.py          # Тесты приложения habits
│
├── 📁 users/           # Приложение для управления пользователями
│ ├── 📁 migrations/    # Миграции базы данных
│ │ └── init.py
│ ├── init.py
│ ├── admin.py          # Регистрация CustomUser в админке
│ ├── apps.py           # Конфигурация приложения Users
│ ├── models.py         # Модель CustomUser
│ ├── views.py          # View для регистрации и профиля
│ ├── serializers.py    # Сериализаторы для пользователей
│ ├── urls.py           # URL маршруты аутентификации
│ └── tests.py          # Тесты приложения users

│
├── 📄 manage.py        # Django CLI утилита
├── 📄 poetry.lock      # Lock-файл Poetry для зависимостей
├── 📄 pyproject.toml   # Конфигурация Poetry и зависимостей
├── 📄 .env             # Переменные окружения (не в репозитории)
├── 📄 .env.sample      # Шаблон файла окружения
├── 📄 .flake8          # Конфигурация линтера Flake8
├── 📄 .gitignore       # Git ignore правила
└── 📄 README.md        # Документация проекта
```
---
## 🚀 Установка и запуск
### Предварительные требования:
- Python 3.8+
- Poetry
- Redis (для Celery)
- PostgreSQL
- 
### 1. Клонируйте репозиторий

git clone https://github.com/SidorovDmitry/coursework_5


### 2. Установите зависимости через Poetry
Зависимости проекта управляются через Poetry. Они перечислены в файле `pyproject.toml`

### 3. Настройте окружение
Создайте файл .env на основе шаблона:`.env.sample `

Заполните его актуальными значениями.

### 4. Примените миграции

`poetry run python manage.py migrate`


### 5. Создайте суперпользователя (опционально)

`poetry run python manage.py createsuperuser`


### 6. Запустите сервер

`poetry run python manage.py runserver`

API будет доступно по адресу: http://127.0.0.1:8000/api/

---

## Тестирование
### Запуск тестов
python manage.py test

### Проверка покрытия
coverage run manage.py test
coverage report
coverage html

### Проверка стиля кода
flake8

---

## Документация:
Для получения дополнительной информации обратитесь к [документации](docs/README.md).

Swagger UI: http://localhost:8000/api/docs/

ReDoc: http://localhost:8000/api/redoc/

 ---

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).




<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Roboto+Mono&weight=600&size=26&duration=3000&pause=1000&color=36BCF7&background=FFFFFF00&center=true&width=600&lines=Dmitriy+Sidorov;Python+Developer+%7C+Django;Django+REST+%7C+Docker+%7C+Git;Welcome+to+my+profile!+%F0%9F%91%8B">
</p>