# coding :utf-8


class Solution:
    """ 
    13. Roman to Integer
    Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）和Ⅿ（1000）
    """

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        size = len(s)
        total = 0

        # for i in range(size - 1):
        #     if romanDict[s[i]] < romanDict[i + 1]:
        #         total -= romanDict[s[i]]
        #     else:
        #         total += romanDict[s[i]]

        # return total + romanDict[s[-1]]

        prev = 0
        total = 0
        for numeral in s[::-1]:
            cur = romanDict[numeral]
            total += cur if cur >= prev else -1 * cur
            prev = cur
        return total
