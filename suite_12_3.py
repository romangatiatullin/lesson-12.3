import unittest
from module_12_2 import TournamentTest
from tests_12_1 import RunnerTest

def skip_if_frozen(test_func):
    def wrapper(*args, **kwargs):
        if args[0].is_frozen:
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return test_func(*args, **kwargs)

    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        pass

    @skip_if_frozen
    def test_run(self):
        pass

    @skip_if_frozen
    def test_walk(self):
        pass

    @skip_if_frozen
    def test_challenge(self):
        pass


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        pass

    @skip_if_frozen
    def test_first_tournament(self):
        pass

    @skip_if_frozen
    def test_second_tournament(self):
        pass

    @skip_if_frozen
    def test_third_tournament(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader.loadTestsFromTestCase(RunnerTest))
    suite.addTest(unittest.TestLoader.loadTestsFromTestCase(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)