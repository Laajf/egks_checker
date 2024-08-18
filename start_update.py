from tg_bot.utils.update_and_send import run_scheduler
import threading


# Запускаем планировщик в отдельном потоке
print("test")
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()