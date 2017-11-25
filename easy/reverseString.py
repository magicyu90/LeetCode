class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        # return ' '.join(s.split()[::-1])[::-1]


print('abcdef'[::-1])
