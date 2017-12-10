class Solution(object):
    """
    387. First Unique Character in a String

    Examples:
    s = "leetcode"
    return 0.
    s = "loveleetcode",
    return 2.
    """

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        # uniqueStr = set(s)
        # print('uniqueStr:', uniqueStr)
        # return s.index(list(uniqueStr)[0]) if uniqueStr else -1
        # ans = -1

        # for i in xrange(len(s)):
        #     print('s:', s)
        #     currentChar = s[i]
        #     print('currentChar:', currentChar)
        #     if currentChar != '@':
        #         if currentChar not in s[i + 1:]:
        #             ans = i
        #             break
        #     s = s.replace(currentChar, '@')
        # return ans

        counter = collections.Counter(s)
        hasUnique = False
        arr = []

        for key in counter.keys():
            if counter[key] == 1:
                hasUnique = True
                arr.append(s.index(key))
        return min(arr) if hasUnique else -1


solution = Solution()
print(solution.firstUniqChar("aabb"))
