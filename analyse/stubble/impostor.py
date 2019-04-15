from reahl.stubble import Impostor, stubclass


class Original:
    pass


@stubclass(Original)
class Fake(Impostor):
    pass


fake = Fake()
assert isinstance(fake, Original)  # True
