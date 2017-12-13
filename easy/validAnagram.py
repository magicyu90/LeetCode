class Solution:
    """
    242. Valid Anagram

    For example,
    s = "anagram", t = "nagaram", return true.
    s = "rat", t = "car", return false.
    """

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        from functools import reduce
        #return reduce(lambda x, y: x ^ y, [ord(a) ^ ord(b) for a, b in zip(s, t)]) == 0
        
        #return sorted(s) == sorted(t)
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item)-ord('a')] += 1
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2


#print(reduce(lambda x, y: ord(x) ^ ord(y), ["a", "b", "c"]))
#reduce(lambda x, y: x ^ y, [ord(a) ^ ord(b) for a, b in zip("ac", "ca")])
