from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.lib.get_path import tick_path, join_path

path = join_path(tick_path, 'ticks.db')
engine = create_engine(f'sqlite:///{path}?check_same_thread=False')

Base = declarative_base()

session = sessionmaker(bind=engine)()

from sqlalchemy import Column, Integer, Float


class Tick:
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(Float)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    volume = Column(Float)

    @classmethod
    def add(cls, bar: list):
        session.add(cls(timestamp=bar[0], open_price=bar[1], high_price=bar[2],
                        low_price=bar[3], close_price=bar[4], volume=bar[5]))
        session.commit()

    @classmethod
    def query_all(cls):
        for row in session.query(cls, cls.timestamp, cls.open_price, cls.high_price,
                                 cls.low_price, cls.close_price, cls.volume).all():
            print(row.timestamp)


newtable = lambda name: type(name.replace('.', '_'), (Base, Tick), {'__tablename__': name.replace('.', '_')})

Base.metadata.create_all(engine)
