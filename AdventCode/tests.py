import unittest
from d01 import puzzle1, puzzle2

# Just to practise writing tests

class TestDay01(unittest.TestCase):

    def test_puzzle1(self):
        self.assertEqual(puzzle1(), 57346)

    def test_puzzle2(self):
        self.assertEqual(puzzle2(), 57345)
    
if __name__ == "__main__":
    unittest.main()