# Just to practice unit tests

import unittest
from medianOfSortedArrays import findMedianSortedArrays

class test_medianOfSortedArrays(unittest.TestCase):
    def test_medianOfSortedArrayss(self):
        self.assertEqual(findMedianSortedArrays([3,4], [1,2]), 2.5)
        self.assertEqual(findMedianSortedArrays([1,3], [2]), 2)

if __name__ == "__main__":
    unittest.main()