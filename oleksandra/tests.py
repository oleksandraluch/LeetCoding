# Just to practice unit tests

import unittest
from medianOfSortedArrays import findMedianSortedArrays
from decode_ways import numDecodings
from longest_substring import lengthOfLongestSubstring

class test_medianOfSortedArrays(unittest.TestCase):
    def test_medianOfSortedArrayss(self):
        self.assertEqual(findMedianSortedArrays([3,4], [1,2]), 2.5)
        self.assertEqual(findMedianSortedArrays([1,3], [2]), 2)

    def test_decode_ways(self):
        self.assertEqual(numDecodings("12"), 2)
        self.assertEqual(numDecodings("226"), 3)
        self.assertEqual(numDecodings("06"), 0)
        self.assertEqual(numDecodings("0088"), 0)
        self.assertEqual(numDecodings("46"), 2)
        
    def test_longest_substring(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)





if __name__ == "__main__":
    unittest.main()