import unittest
from main import main
class TestMain(unittest.TestCase):
    def test_import(self):
        self.assertTrue(callable(main))
if __name__ == '__main__': unittest.main()
