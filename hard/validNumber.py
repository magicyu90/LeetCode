# coding :utf-8
class Solution:
    """
    Validate if a given string is numeric.

    Some examples:
    "0" => true
    " 0.1 " => true
    "abc" => false
    "1 a" => false
    "2e10" => true
    """

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        