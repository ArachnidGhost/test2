import os
import time
from threading import Thread
import schedule
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

def clear_database():
    from django.core.management import call_command
    call_command('flush', '--noinput')  # Это удалит все данные из базы данных

def run_scheduler():
    schedule.every().day.at("00:00").do(clear_database)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Ждем 1 минуту перед следующей проверкой

# Запускаем планировщик в отдельном потоке
scheduler_thread = Thread(target=run_scheduler)
scheduler_thread.daemon = True  # Позволяет завершить поток при завершении основного приложения
scheduler_thread.start()

application = get_wsgi_application()
