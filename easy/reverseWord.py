class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = ' '.join([word[::-1] for word in s.split(' ')])
        return words


solution = Solution()
solution.reverseWords("Let's take LeetCode contest")
