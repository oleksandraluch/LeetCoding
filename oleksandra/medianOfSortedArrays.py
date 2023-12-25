# Nov 30, 2023
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

# O(n log(n)) solution
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    # merge lists   
    lst = nums1 + nums2
    lst.sort() # O(n log(n))

    lst_len = len(lst)
    if lst_len % 2:
        # median element exists
        return lst[lst_len//2]
    else:
        # median to be calculated
        return (lst[lst_len//2] + lst[lst_len//2 - 1]) / 2