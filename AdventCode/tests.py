# Just to practise writing tests

import unittest
from d01 import puzzle1, puzzle2
from d02 import sum_valid_games, sum_powers_of_games, games
from d03 import get_adjacent_indexes, sum_all_adjacent_numbers, get_adjacent_indexes_and_nums, sum_gear_ratios

class TestDay01(unittest.TestCase):

    def test_puzzle1(self):
        self.assertEqual(puzzle1(), 57346)

    def test_puzzle2(self):
        self.assertEqual(puzzle2(), 57345)
    
class TestDay02(unittest.TestCase):

    def test_puzzle1(self):
        self.assertEqual(sum_valid_games(games), 2913)

    def test_puzzle2(self):
        self.assertEqual(sum_powers_of_games(games), 55593)

class testDay03(unittest.TestCase):

    def test_get_adjacent_indexes(self):
        self.assertEqual(get_adjacent_indexes("...."), [])
        self.assertEqual(get_adjacent_indexes(""), [])
        self.assertEqual(get_adjacent_indexes("83@.*."), [2, 1, 3, 4, 5])
        self.assertEqual(get_adjacent_indexes("..83@.*.951*..984*111..-@"), [4, 3, 5, 6, 7, 11, 10, 12, 17, 16, 18, 23, 22, 24])
    
    def test_puzzle1(self):
        self.assertEqual(sum_all_adjacent_numbers(), 528819)

    def test_get_adjacent_indexes_and_nums(self):
        self.assertEqual(get_adjacent_indexes_and_nums(".2)(&).."), {0: ['2'], 1: ['2'], 2: ['2']})
        self.assertEqual(get_adjacent_indexes_and_nums("...231,*i...5"), {2: ['231'], 3: ['231'], 4: ['231'], 5: ['231'], 6: ['231'], 11: ['5'], 12: ['5']})
        self.assertEqual(get_adjacent_indexes_and_nums("...231,67*i...5"), {2: ['231'], 3: ['231'], 4: ['231', '67'], 5: ['231'], 6: ['231', '67'], 7: ['67'], 8: ['67'], 9: ['67'], 13: ['5'], 14: ['5']})

    def test_puzzle2(self):
        self.assertEqual(sum_gear_ratios(), 80403602)

if __name__ == "__main__":
    unittest.main()