# Problem: https://leetcode.com/problems/decode-ways/description/?envType=daily-question&envId=2023-12-25

# Constraints:
#     1 <= s.length <= 100
#     s contains only digits and may contain leading zero(s).


#def numDecodings(self, s):
def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    decode_ways = 0
    valid_nums = list(range(1, 27))

    # check if the first digit is 0
    if s[0] == '0': return decode_ways # if the first digit is 0, there's no way to decode s

    for index, curr_num in enumerate(s):
        if int(curr_num) in valid_nums:
            decode_ways += 1
            # append next num to curr_num and validate it
            if index < len(s) - 1:
                curr_num += s[index + 1]
                if curr_num in valid_nums: 
                    decode_ways += 1
    return decode_ways