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
        return s[::-1]
        # return ' '.join(s.split()[::-1])[::-1]


print('abcdef'[::-1])
