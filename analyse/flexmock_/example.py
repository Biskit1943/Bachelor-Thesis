import sys
import unittest
import flexmock

from my_package.my_mock_module import (
    NotMocked,
    Helper,
)


class TestFlexmock(unittest.TestCase):
    def setUp(self):
        self.mock = flexmock(NotMocked)
        self.not_mocked = NotMocked()

    def test_print_foo(self):
        self.mock.should_receive('print_foo').replace_with(lambda: print('foo'))
        self.not_mocked.print_foo()  # print_foo wurde ersetzt

        output = sys.stdout.getvalue().strip()  # stdout von unittest
        self.assertEquals(output,'foo')

    def test_return_42(self):
        self.mock.should_receive('return_42').and_return(42)
        self.assertIs(42, self.not_mocked.return_42())  # returned jetzt immer 42

    def test_raise_error(self):
        self.mock.should_receive('raise_error').and_raise(BaseException, 'success')
        self.assertRaises(BaseException, self.not_mocked.raise_error)

    def test_call_internal_function(self):
        self.mock.should_call('_internal_function').once()
        self.not_mocked.call_internal_function()

    def test_call_internal_function_n_times(self):
        self.mock.should_call('_internal_function').times(3)
        self.not_mocked.call_internal_function_n_times(3)

    def test_call_helper_help(self):
        helper_mock = flexmock(Helper())
        helper_mock.should_receive('help').replace_with(lambda: True)
        #helper_mock.should_call('help').once()  # Check ob help aufgerufen wurde

        self.not_mocked.call_helper_help(helper_mock)

    def test_return_false_filepath(self):
        import os
        new_os = flexmock(os)
        new_os.should_receive('path.abspath').and_return('/foo/bar/baz.py')
        self.assertEqual(self.not_mocked.return_false_filepath(), '/foo/bar/baz.py')


if __name__ == '__main__':
    unittest.main(buffer=True)
