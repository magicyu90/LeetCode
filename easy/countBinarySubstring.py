# coding:utf-8
class Solution:
    """
    696. Count Binary Substrings
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's:
    "0011", "01", "1100", "10", "0011", and "01".

    Notice that some of these substrings repeat and are counted the number of times they occur.

    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
    """

    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        count = [0, 0]
        i = 0
        while i < len(s):
            count[0] = 0
            while i < len(s) and s[i] == s[0]:
                count[0] += 1
                i += 1
            ans += min(count[0], count[1])
            count[1] = 0
            while i < len(s) and s[i] != s[0]:
                count[1] += 1
                i += 1
            ans += min(count[0], count[1])
        return ans


solution = Solution()
print(solution.countBinarySubstrings("10101"))
