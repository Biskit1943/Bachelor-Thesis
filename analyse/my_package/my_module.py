"""my_module.py"""
from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

do_something_which_does_not_exist = None


def my_pow(a, b):
    result = a
    for _ in range(1, b):
        result = result * a

    return result


class Item(Base):
    __tablename__ = 'items'

    id_ = Column('id', Integer, primary_key=True)
    name = Column(String(64))
    storage_location = Column(Integer)
    amount = Column(Integer)

    def do_something(self):
        return do_something_which_does_not_exist(self)

    def __repr__(self):
        return f'item<{self.id_}, {self.name}, {self.storage_location}, {self.amount}>'


Base.metadata.create_all(engine)

if __name__ == '__main__':
    item = Item(id_=1, name='name', storage_location=1, amount=1)
    session.add(item)
    session.commit()
    print(session.query(Item).all())
    print(len(session.new))
