# coding:utf-8
import collections
from functools import reduce
import operator


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 我的思路：借助Collection.Counter方法
        # if s is in t:
        # return t[: t.index(s)] + t[t.index(s) + len(s):]
        # return list((collections.Counter(t) - collections.Counter(s)))[0]
        # s, t = sorted(s), sorted(t)
        # return t[-1] if s == t[:-1] else [x[1] for x in zip(s, t) if x[0] != x[1]][0]
        return chr(reduce(operator.xor, map(ord, s + t)))


solution = Solution()
print(solution.findTheDifference('abcc', 'abjcc'))

print([x for x in zip('bcd', 'becd')])
