import unittest

# custom libs
from packages import process


# tests
class TestProcess(unittest.TestCase):

    def test_queue(self):
        '''Make sure multiprocessing.Queue works as it should'''
        # run deploy func on simple builtin pow func
        results = process.deploy(
            pow,
            base=2,
            exp=2,
        )

        # confirm returned results match
        self.assertEqual(results, pow(2, 2))


if __name__ == '__main__':
    unittest.main()
