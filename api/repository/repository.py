from sqlalchemy import create_engine, Column,String,Integer,BIGINT
from sqlalchemy.orm import declarative_base, sessionmaker
import json
# Пример строки подключения
#engine = create_engine('postgresql://postgres:11111@localhost:5432/tg_bot_egks')

# Пример использования
#connection = engine.connect()
#print("все хорошо")

class postgresql:


    @staticmethod
    def bd_create(data):
        try:
            data_base_url = 'postgresql://postgres:11111@db:5432/tg_bot_egks'
            engine = create_engine(data_base_url)
            Base = declarative_base()

            class data_card(Base):
                __tablename__ = "users"
                number_card = Column(Integer)
                chat_id = Column(Integer)
                chat_id_number_card = Column(Integer, primary_key=True)
                money = Column(Integer)

            Session = sessionmaker(bind=engine)
            session = Session()
            user = data_card(number_card=data.get("ticket_number"), chat_id="chat_id",
                             chat_id_number_card=data.get("ticket_number") + "chat_id", money=data.get("balance"))
            session.add(user)

            session.commit()
            session.close()
            return True

        except:
            return "Пользователь не создан,введите коректные данные"




    @staticmethod
    def bd_read():
        data_base_url = 'postgresql://postgres:11111@db:5432/tg_bot_egks'
        engine = create_engine(data_base_url)
        Base = declarative_base()

        class data_card(Base):
            __tablename__ = "users"
            number_card = Column(String)
            chat_id = Column(String)
            chat_id_number_card = Column(String, primary_key=True)
            money = Column(String)

        Session = sessionmaker(bind=engine)
        session = Session()
        users = session.query(data_card).all()
        session.close()
        users_list = [
            {
                "number_card": user.number_card,
                "chat_id": user.chat_id,
                "chat_id_number_card": user.chat_id_number_card,
                "money": user.money
            }
            for user in users
        ]

        # Преобразование в JSON
        users_json = json.dumps(users_list, indent=4)

        # Отладочный вывод
        print(f"вот юзеры: {users_json}")
        users_list = json.loads(users_json)

        return users_list

