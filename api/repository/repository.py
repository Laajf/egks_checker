from sqlalchemy import create_engine, Column,String,Integer,BIGINT
from sqlalchemy.orm import declarative_base, sessionmaker

# Пример строки подключения
#engine = create_engine('postgresql://postgres:11111@localhost:5432/tg_bot_egks')

# Пример использования
#connection = engine.connect()
#print("все хорошо")

class postgresql:


    @staticmethod
    def bd_update(data):
        data_base_url = 'postgresql://postgres:11111@localhost:5432/tg_bot_egks'
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

        user = data_card(number_card= data.get("ticket_number"),chat_id= data.get("n"),chat_id_number_card= data.get("n") ,money= data.get("balance") )
        session.add(user)

        session.commit()

    @staticmethod
    def bd_read():
        data_base_url = 'postgresql://postgres:11111@localhost:5432/tg_bot_egks'
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
        users = session.query(data_card).all()
        return users

