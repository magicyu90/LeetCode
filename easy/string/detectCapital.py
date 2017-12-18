# coding:utf-8
class Solution:
    """
    520. Detect Capital
    Example 1:
    Input: "USA"
    Output: True

    Example 2:
    Input: "FlaG"
    Output: False
    """

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 我的思路：长度为1肯定True 否则全部大写 or 全部小写 or 首字母大写其余小写为TRUE
        return True if len(word) == 1 else word.islower() or word.isupper() or (word[:1].isupper() and word[1:].islower())
        # return word.isupper() or word.islower() or word.istitle()


solution = Solution()
print(solution.detectCapitalUse('ChinA'))
