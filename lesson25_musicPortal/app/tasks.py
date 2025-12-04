from celery import shared_task
import time

@shared_task
def test_celery_task():
    time.sleep(3)
    print("🎉 Celery worker выполнил задачу!")
    return "Task completed!"

@shared_task
def beat_test_task():
    print("⏰ Celery Beat запустил задачу!")
    return "Beat OK"
