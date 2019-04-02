import pytest

from my_package.my_module import (
    Item,
    session,
)

class TestMyDatabase:
    @pytest.fixture
    def setUp_tearDown(self):
        # setUp
        self.item = Item(id_=1, name='name', storage_location=7, amount=3)
        yield self.item
        # tearDown
        session.close()

    def test_creation(self, setUp_tearDown):
        session.add(self.item)
        session.commit()

        assert len(session.new) is 0, 'Lenght is not 0, session is dirty'
        assert session.query(Item).first() is self.item, 'Item is not in databse'

    def test_external_function(self, setUp_tearDown, monkeypatch):
        def mock_return(something):
            return 42

        monkeypatch.setattr(Item, 'do_something', mock_return)
        assert self.item.do_something() is 42, 'Do something wasn\'t patched'


if __name__ == '__main__':
    pytest.main()
