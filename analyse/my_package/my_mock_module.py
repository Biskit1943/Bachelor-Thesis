import os


class Helper:
    """Diese Klasse simuliert eine Klasse die noch nicht geschrieben wurde"""
    pass


class NotMocked:
    """Originale Klasse.
    Die Methodennamen geben an was sie eigentlich machen sollten
    """
    def print_foo(self):
        print("I should print foo, instead I print this!")

    def return_42(self):
        return 21

    def raise_error(self):
        return

    def _internal_function(self):
        return

    def call_internal_function(self):
        self._internal_function()

    def call_internal_function_n_times(self, n):
        for _ in range(0, n):
            self._internal_function()

    def call_helper_help(self, h: Helper):
        assert isinstance(h, Helper)
        assert h.help() is True

    def return_false_filepath(self):
        """Diese Methode soll /foo/bar/baz.py zurueckgeben"""
        return os.path.abspath(__file__)
