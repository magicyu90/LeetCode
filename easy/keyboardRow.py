class Solution:
    """
    500. Keyboard Row
    
    Example 1:
    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]
    """
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for word in words:
            if check(word) == True:
                ans.append(word)
        return ans


def check(element):
    """
    :type element: str
    """
    wordList = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    isExist = False
    for word in set(wordList):
        if all(c.upper() in word for c in element):
            isExist = True
            break
    return isExist


def check2(element):
    line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    w = set(element.lower())
    if w <= (line1) or w <= (line2) or w <= (line3):
        return True
    else:
        return False


print(check('cccd'))
print(check2('cccd'))
solution = Solution()
print(solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))
