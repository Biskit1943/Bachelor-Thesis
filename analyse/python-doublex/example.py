import sys
import unittest

from doublex import (
    Stub,
    Spy,
    ProxySpy,
    assert_that,
    is_,
    called,
)


from my_package.my_mock_module import (
    NotMocked,
    Helper,
)


class TestFlexmock(unittest.TestCase):
    def setUp(self):
        pass

    def test_print_foo(self):
        with Stub(NotMocked) as stub:
            stub.print_foo().delegates(lambda: print('foo'))
        stub.print_foo()  # Das Duplikat kann nun print_foo()
        self.assertEquals(sys.stdout.getvalue(),'foo\n')

    def test_return_42(self):
        with Stub(NotMocked) as stub:
            stub.return_42().returns(42)

        assert_that(stub.return_42(), is_(42))

    def test_raise_error(self):
        with Stub(NotMocked) as stub:
            stub.raise_error().raises(BaseException('success'))

        self.assertRaises(BaseException, stub.raise_error)

    def test_call_internal_function(self):
        spy = ProxySpy(NotMocked())

        spy.call_internal_function()
        assert_that(spy._internal_function, called())
        '''
        Das ist mit doublex nicht moeglich, der Error ist folgender:

        Expected: these calls:
                NotMocked._internal_function(ANY_ARG)
            but: calls that actually ocurred were:
                NotMocked.call_internal_function()
        '''


    def test_call_internal_function_n_times(self):
        pass
        '''
        Hier kommt der gleiche Fehler wie bei test_call_internal_function
        '''

    def test_call_helper_help(self):
        with Stub() as helper:
            helper.help().returns(True)

        self.assertTrue(NotMocked().call_helper_help(helper))
        '''
        Dieser Test wird auch fehlschlagen, da es nicht moeglich ist vor zu
        taeuschen eine Klasse zu sein. Ein doublex Objekt ist immer ein
        Duplikat aber niemals die Klasse selbst.
        '''

    def test_return_false_filepath(self):
        with Stub(NotMocked) as stub:
            stub.return_false_filepath().returns('/foo/bar/baz.py')

        assert_that(stub.return_false_filepath(), is_('/foo/bar/baz.py'))
        '''
        Es ist mit doublex leider nicht moeglich globale Objekte oder Module
        zu ersetzen. Lediglich ein Duplikat koennte als parameter uebergeben
        werden.
        '''


if __name__ == '__main__':
    unittest.main(buffer=True)
