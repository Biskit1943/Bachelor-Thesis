import unittest
from reahl.stubble import (
        exempt,
        replaced,
        stubclass,
)
from reahl.stubble.intercept import (
    CallMonitor,
    SystemOutStub,
)

from my_package.my_mock_module import (
    NotMocked,
    Helper,
)

@stubclass(NotMocked)
class Mocked(NotMocked):
    def print_foo(self):
        print("foo")

    def return_42(self):
        return 42

    def raise_error(self):
        raise BaseException("success")


@stubclass(Helper)
class MockedHelper(Helper):
    @exempt
    def help(self):
        """Loest das Problem zwar, aber wenn die Funktion existiert wird nicht
        die signatur ueberprueft.
        """
        return True


class TestStubble(unittest.TestCase):
    def setUp(self):
        self.mock = Mocked()

    def test_print_foo(self):
        with SystemOutStub() as monitor:
            self.mock.print_foo()

        assert monitor.captured_output == 'foo\n'

    def test_return_42(self):
        self.assertEqual(self.mock.return_42(), 42)

    def test_raise_error(self):
        self.assertRaises(BaseException, self.mock.raise_error)

    def test_call_internal_function(self):
        with CallMonitor(self.mock._internal_function) as monitor:
            self.mock.call_internal_function()

        self.assertIs(monitor.times_called, 1)
        self.assertEqual(monitor.calls[0].args, ())
        self.assertEqual(monitor.calls[0].kwargs, {})
        self.assertIs(monitor.calls[0].return_value, None)

    def test_call_internal_function_n_times(self):
        with CallMonitor(self.mock._internal_function) as monitor:
            self.mock.call_internal_function_n_times(4)

        self.assertIs(monitor.times_called, 4)
        self.assertEqual(monitor.calls[0].args, ())
        self.assertEqual(monitor.calls[0].kwargs, {})
        self.assertIs(monitor.calls[0].return_value, None)

    def test_call_helper_help(self):
        helper = MockedHelper()
        with CallMonitor(helper.help) as monitor:
            self.mock.call_helper_help(helper)

        self.assertIs(monitor.times_called, 1)
        self.assertEqual(monitor.calls[0].args, ())
        self.assertEqual(monitor.calls[0].kwargs, {})
        self.assertIs(monitor.calls[0].return_value, True)

    def fake_os_path_abspath(self, path):
        return "/foo/bar/baz.py"

    def test_return_false_filepath(self):
        from my_package.my_mock_module import os as my_os
        with replaced(my_os.path.abspath, self.fake_os_path_abspath, on=my_os.path):
            self.assertEqual("/foo/bar/baz.py", self.mock.return_false_filepath())
        self.assertNotEqual("/foo/bar/baz.py", self.mock.return_false_filepath())


if __name__ == '__main__':
    unittest.main()
