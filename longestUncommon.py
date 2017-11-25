class Solution:
    """
    521. Longest Uncommon Subsequence I
    Input: "aba", "cdc"
    Output: 3
    Explanation: The longest uncommon subsequence is "aba" (or "cdc"),
    because "aba" is a subsequence of "aba",
    but not a subsequence of any other strings in the group of two strings.
    """

    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """

        return -1 if a == b else max(len(a), len(b))


solution = Solution()
print('ans:', solution.findLUSlength("aba", "cdc"))
