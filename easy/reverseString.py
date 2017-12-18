class Solution:
    """
    344. Reverse String

    Example:
    Given s = "hello", return "olleh".
    """

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s[::-1]
        # return ' '.join(s.split()[::-1])[::-1]
        r = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1
        return "".join(r)


solution = Solution()
print(solution.reverseString('abcdef'))
