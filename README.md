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
- 🧪 Покрытие тестами и линтинг
- 🚀 CI/CD через GitHub Actions


---

## 🛠 Технологический стек

- **Backend** : Django 4.2+, Django REST Framework
- **База данных** : PostgreSQL
- **Аутентификация** : JWT (Simple JWT)
- **Очереди задач** : Celery + Redis
- **Документация** : DRF Spectacular (Swagger/Redoc)
- **Уведомления** : Telegram Bot API
- **CORS** : django-cors-headers
- **Линтинг** : GitHub Actions + SSH Deploy
- **CI/CD**: django-cors-headers
- **Зависимости**: Poetry / Pip

---

## 📁 Структура проекта
Ниже представлена структура проекта с пояснениями к каждой папке и файлу:

<details> <summary><strong>📦 coursework_5/ — Корневая директория проекта</strong></summary>

```
coursework_5/
├── .github/                # ⚙️ Конфигурация CI/CD через GitHub Actions
│   └── workflows/          # 🔁 Workflows для автоматизации (тесты, деплой)
│       └── deploy.yml      # 🚀 Скрипт деплоя на сервер через SSH

├── config/                 # ⚙️ Основная конфигурация Django и Celery
│   ├── __init__.py         # Инициализация пакета
│   ├── settings.py         # Настройки Django: базы, приложения, middleware
│   ├── urls.py             # Главный URL-роутер проекта
│   ├── wsgi.py             # WSGI-конфигурация для продакшн-сервера
│   ├── asgi.py             # ASGI-конфигурация для async-сервера
│   └── celery.py           # Настройка Celery для фоновых задач

├── habits/                 # 📌 Приложение для управления привычками
│   ├── migrations/         # 📦 Миграции базы данных
│   ├── admin.py            # Регистрация моделей в Django Admin
│   ├── apps.py             # Конфигурация приложения habits
│   ├── models.py           # Модели Habit, Reward и связанные сущности
│   ├── views.py            # ViewSet'ы и API endpoints
│   ├── serializers.py      # DRF-сериализаторы для моделей
│   ├── urls.py             # URL-маршруты приложения habits
│   ├── permissions.py      # Кастомные права доступа
│   ├── services.py         # Бизнес-логика и вспомогательные функции
│   ├── tasks.py            # Celery-задачи для Telegram-уведомлений
│   └── tests.py            # Тесты для приложения habits

├── users/                  # 👤 Приложение для управления пользователями
│   ├── migrations/         # 📦 Миграции базы данных
│   ├── admin.py            # Регистрация модели CustomUser
│   ├── apps.py             # Конфигурация приложения users
│   ├── models.py           # Модель CustomUser
│   ├── views.py            # Views для регистрации и профиля
│   ├── serializers.py      # DRF-сериализаторы для пользователей
│   ├── urls.py             # URL-маршруты аутентификации
│   └── tests.py            # Тесты для приложения users

├── media/                  # 🖼️ Хранилище загружаемых файлов (если используется)
├── static/                 # 🎨 Статические файлы проекта (CSS, JS, изображения)
├── staticfiles/            # 📦 Сборка статических файлов после collectstatic

├── coverage/               # 📊 HTML-отчёты покрытия тестами (если используется)
├── docker-compose.yml      # 🐳 Конфигурация Docker-сервисов (Postgres, Redis, Django)
├── Dockerfile              # 🐳 Инструкция сборки образа Django-приложения
├── nginx.conf              # 🌐 Конфигурация Nginx для продакшн-сервера
├── .dockerignore           # 🚫 Исключения для Docker-сборки
├── .env                    # 🔐 Переменные окружения (не коммитится)
├── .env.sample             # 📄 Шаблон .env для настройки окружения
├── .flake8                 # 🧹 Конфигурация линтера Flake8
├── .gitignore              # 🚫 Список файлов, игнорируемых Git
├── manage.py               # 🛠️ Django CLI для запуска команд
├── poetry.lock             # 🔒 Lock-файл Poetry для фиксированных версий зависимостей
├── pyproject.toml          # 📦 Конфигурация Poetry и зависимостей проекта
├── requirements.txt        # 📋 Альтернативный список зависимостей (если используется)
└── README.md               # 📘 Документация проекта

```
</details>

---
## 🚀 Установка и запуск
<details> <summary><strong>🚀 Установка и запуск — Инструкция </strong></summary>
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

API будет доступно по адресу: http://127.0.0.1:8000/
</details>
---

## 🧪 Тестирование
### Запуск тестов
``` python manage.py test ```

### Проверка покрытия
```
coverage run manage.py test
coverage report
coverage html
```


### Проверка стиля кода
flake8

---

## 📚 Документация
Для получения дополнительной информации обратитесь к [документации](docs/README.md).

Swagger UI: http://localhost:8000/api/docs/

ReDoc: http://localhost:8000/api/redoc/

 ---
## 🚀 CI/CD
### Проект включает GitHub Actions workflow:
- Автоматическое тестирование при push
- Проверка стиля кода
- Деплой на сервер через SSH)
- Уведомление в Telegram после успешного деплоя
### Файл workflow: ```.github/workflows/deploy.yml```

### Проект работает на   [Habit Tracker](http://89.169.166.129/api/docs/)

 Проект оптимизирован для деплоя размером контейнеров и скоротью разворачивания на сервере

 ---
## 📬 Уведомления через Telegram
### Для отправки напоминаний используется Telegram Bot API. 
### Настройка:
1. Создайте бота через [@BotFather](https://t.me/BotFather)
2. Получите токен и добавьте в ```.env```:
```commandline
TELEGRAM_TOKEN=your_bot_token
TELEGRAM_TO=your_chat_id
```
3. Убедитесь, что пользователь начал диалог с ботом (отправил ```/start```)
4. Запустите Celery worker:
```
poetry run celery -A config worker --loglevel=info
```
 ---
## ⏱ Периодические задачи
### Для плановых напоминаний используется Celery Beat:
```commandline
poetry run celery -A config beat --loglevel=info
```
### Задачи определены в ```habits/tasks.py``` и активируются по расписанию.

 ---
## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).




<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Roboto+Mono&weight=600&size=26&duration=3000&pause=1000&color=36BCF7&background=FFFFFF00&center=true&width=600&lines=Dmitriy+Sidorov;Python+Developer+%7C+Django;Django+REST+%7C+Docker+%7C+Git;Welcome+to+my+profile!+%F0%9F%91%8B">
</p>