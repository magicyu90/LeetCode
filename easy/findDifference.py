import collections


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # if s is in t:
        # return t[: t.index(s)] + t[t.index(s) + len(s):]
        return list((collections.Counter(t) - collections.Counter(s)))[0]
