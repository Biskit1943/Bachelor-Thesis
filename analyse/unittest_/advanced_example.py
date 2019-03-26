import unittest
import unittest.mock as mock

from my_package.my_module import (
    Item,
    session
)

class TestMyDatabase(unittest.TestCase):
    def setUp(self):
        self.item = Item(id_=1, name='name', storage_location=7, amount=3)

    def test_creation(self):
        session.add(self.item)
        session.commit()

        self.assertIs(len(session.new), 0)
        self.assertEqual(session.query(Item).first(), self.item)

    @mock.patch('my_package.my_module.do_something_which_does_not_exist')
    def test_external_function(self, mock_do_something_which_does_not_exist):
        mock_do_something_which_does_not_exist.return_value = 42


        self.assertIs(self.item.do_something(), 42)
        mock_do_something_which_does_not_exist.assert_called_with(self.item)

    def tearDown(self):
        session.close()

if __name__ == '__main__':
    unittest.main()
