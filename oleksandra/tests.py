# Just to practice unit tests

import unittest
from medianOfSortedArrays import findMedianSortedArrays
from decodeWays import numDecodings

class test_medianOfSortedArrays(unittest.TestCase):
    def test_medianOfSortedArrayss(self):
        self.assertEqual(findMedianSortedArrays([3,4], [1,2]), 2.5)
        self.assertEqual(findMedianSortedArrays([1,3], [2]), 2)

    def test_decodeWays(self):
        self.assertEqual(numDecodings("12"), 2)
        self.assertEqual(numDecodings("226"), 3)
        self.assertEqual(numDecodings("06"), 0)
        self.assertEqual(numDecodings("0088"), 0)
        self.assertEqual(numDecodings("46"), 2)
        



if __name__ == "__main__":
    unittest.main()