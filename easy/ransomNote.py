class Solution:
    """
    383. Ransom Note

    Note:
    You may assume that both strings contain only lowercase letters.
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
    """

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections

        ransomCollection = collections.Counter(ransomNote)
        magazineCollection = collections.Counter(magazine)
        
        for ransomKey in ransomCollection.keys():
            if not magazineCollection[ransomKey] or ransomCollection[ransomKey] > magazineCollection[ransomKey]:
                return False

        return True


solution = Solution()
print(solution.canConstruct("aa", "acab"))
