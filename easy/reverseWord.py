# coding:utf-8
class Solution:
    """
    557. Reverse Words in a String III
    Example 1:
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    """

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = ' '.join([word[::-1] for word in s.split(' ')])
        return words


solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))
