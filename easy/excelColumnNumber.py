# coding:utf-8
class Solution:
    """
    171. Excel Sheet Column Number
    For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    """

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import math
        ans = 0
        index = 0
        s = s[::-1]
        for word in s:
            ans += math.pow(26, index) * ((ord(word)) - 64)
            index += 1

        return int(ans)


solution = Solution()
print(solution.titleToNumber("AAA"))
