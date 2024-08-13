from sqlalchemy import create_engine

# Пример строки подключения
engine = create_engine('postgresql://postgres:11111@localhost:5432/tg_bot_egks')

# Пример использования
connection = engine.connect()
print("все хорошо")