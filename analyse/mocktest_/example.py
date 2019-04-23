import sys
from mocktest import *

from my_package.my_mock_module import (
    NotMocked,
    Helper,
)


class TestMocktest(TestCase):
    def setUp(self):
        self.not_mocked = NotMocked()

    def test_print_foo(self):
        expect(self.not_mocked).print_foo().then_return(lambda: print('foo'))
        self.not_mocked.print_foo()

        self.assertEqual(sys.stdout.getvalue(), 'foo\n')

    def test_return_42(self):
        when(self.not_mocked).return_42().then_return(42)
        self.assertEqual(self.not_mocked.return_42(), 42)


    def test_raise_error(self):
        def raise_error():
            raise BaseException('success')

        modify(self.not_mocked).raise_error = raise_error
        self.assertRaises(BaseException, self.not_mocked.raise_error,
                          message='success', matching=r'.*')

    def test_call_internal_function(self):
        expect(self.not_mocked)._internal_function.once()
        self.not_mocked.call_internal_function()

    def test_call_internal_function_n_times(self):
        expect(self.not_mocked)._internal_function.thrice()
        self.not_mocked.call_internal_function_n_times(3)

    def test_call_helper_help(self):
        helper = Helper()
        when(helper).help.then_return(True).once()
        self.not_mocked.call_helper_help(helper)

    def test_return_false_filepath(self):
        import os
        when(os.path).abspath.then_return('/foo/bar/baz.py')
        self.assertEqual('/foo/bar/baz.py', self.not_mocked.return_false_filepath())


if __name__ == '__main__':
    import unittest
    unittest.main(buffer=True)
