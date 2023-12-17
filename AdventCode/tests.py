import unittest
from d01 import puzzle1, puzzle2
from d02 import sum_valid_games, games
# Just to practise writing tests

class TestDay01(unittest.TestCase):

    def test_puzzle1(self):
        self.assertEqual(puzzle1(), 57346)

    def test_puzzle2(self):
        self.assertEqual(puzzle2(), 57345)
    
class TestDay02(unittest.TestCase):

    def test_puzzle1(self):
        self.assertEqual(sum_valid_games(games), 2913)

if __name__ == "__main__":
    unittest.main()