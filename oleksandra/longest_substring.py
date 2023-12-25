# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Longest substring without repeating chars

# Constraints:

#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.


# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """

#     longest_substr = ""
#     curr_substr = ""

#     for symbol in s:
#         if not symbol in curr_substr:
#             curr_substr += symbol
#         else:
#             if len(curr_substr) > len(longest_substr): longest_substr = curr_substr

#     return longest_substr

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    longest_substr = ""
    curr_substr = ""

    for index, leading in enumerate(s):
        curr_substr = leading
        if index < len(s) - 1:
            for symbol in s[index:]:
                if not symbol in curr_substr:
                    curr_substr += symbol
                else:
                    if len(curr_substr) > len(longest_substr): longest_substr = curr_substr
                    curr_substr = ""
    print(longest_substr)
    return len(longest_substr)

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("9908"))
