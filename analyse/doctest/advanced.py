"""my_module"""
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
    """
    >>> my_pow(2, 2)
    4
    >>> my_pow(4, 8)
    65536
    """
    result = a
    for _ in range(1, b):
        result = result * a

    return result


class Item(Base):
    """
    Da Doctest keine Fixtures unterstuetzt muss hier der setUp Code stehen:
    >>> Base.metadata.create_all(engine)
    >>> item = Item(id_=1, name='name', storage_location=1, amount=1)
    >>> session = Session()
    >>> session.add(item)
    >>> session.commit()


    Check ob das item commited wurde
    >>> len(session.new)
    0

    Check ob das item in der Datenbank ist.
    Das item wird mit seiner __repr__() Methode representiert, da die
    Werte bekannt sind kann ueberprueft werden ob diese uebereinstimmen.
    >>> session.query(Item).first()
    item<1, name, 1, 1>

    do_something existiert nicht, da mit Doctest kein Mock erstellt werden
    kann wird auf die Exception ueberprueft.
    >>> item.do_something()
    Traceback (most recent call last):
        ...
    TypeError: 'NoneType' object is not callable

    Hier wird der tearDown Code ausgefuehrt
    >>> session.close()
    """
    __tablename__ = 'items'

    id_ = Column('id', Integer, primary_key=True)
    name = Column(String(64))
    storage_location = Column(Integer)
    amount = Column(Integer)

    def do_something(self):
        return do_something_which_does_not_exist(self)

    def __repr__(self):
        return f'item<{self.id_}, {self.name}, {self.storage_location}, {self.amount}>'

if __name__ == '__main__':
    import doctest
    # Fuehrt die internen Tests aus
    doctest.testmod()
    # Fuehrt die externen Tests aus
    doctest.testfile('advanced.txt')
