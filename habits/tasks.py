import json

import requests
from celery import shared_task
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from config.settings import BOT_TOKEN, TG_URL
from habits.models import Habits
from habits.services import is_time_to_send_reminder


@shared_task
def time_habit(habit_id):
    """Отправка уведомления для конкретной привычки"""
    try:
        habit = Habits.objects.get(id=habit_id)

        # Проверяем наличие владельца и telegram ID
        if not habit.owner:
            print(f"Привычка {habit_id} не имеет владельца")
            return

        if not habit.owner.tg_id:
            print(f"Владелец {habit.owner.username} не имеет telegram ID")
            return

        print(f"Проверка времени для привычки {habit_id}: {is_time_to_send_reminder(habit)}")

        # В задаче Celery тоже используем проверку времени
        if is_time_to_send_reminder(habit):
            params = {
                "text": f"Напоминание: {habit.action} в {habit.start_time}",
                "chat_id": habit.owner.tg_id,
            }
            response = requests.get(f"{TG_URL}{BOT_TOKEN}/sendMessage", params=params)
            print(f"Ответ Telegram: {response.json()}")
        else:
            print(f"Время для привычки {habit_id} не подходит для отправки")

    except Habits.DoesNotExist:
        print(f"Привычка с id {habit_id} не найдена")
    except Exception as e:
        print(f"Ошибка при отправке уведомления для привычки {habit_id}: {e}")


def setup_habit_tasks():
    """Создание/обновление периодических задач для привычек"""
    for habit in Habits.objects.all():
        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=str(habit.start_time.minute),
            hour=str(habit.start_time.hour),
            day_of_week="*",
            day_of_month="*",
            month_of_year="*",
            timezone="Europe/Moscow",
        )

        task_name = f"Send a reminder about {habit}"

        PeriodicTask.objects.update_or_create(
            name=task_name,
            defaults={
                "crontab": schedule,
                "task": "habits.tasks.time_habit",
                "args": json.dumps([habit.id]),
                "enabled": True,
            },
        )
