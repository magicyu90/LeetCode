class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        # nums_copy = [n for n in nums]
        # nums_copy.reverse()

        # nums_dict = {num: index + 1 for index, num in enumerate(nums_copy)}

        # output = []

        # for n in nums:
        #     if nums_dict[n] == 1:
        #         output.append("Gold Medal")
        #     if nums_dict[n] == 2:
        #         output.append("Silver Medal")
        #     if nums_dict[n] == 3:
        #         output.append("Bronze Medal")
        #     else:
        #         output.append(str(nums_dict[n]))
        # return output

        # 大神写法:
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + \
            list(map(str, range(4, len(nums) + 1)))
        return list(map(dict(zip(sort, rank)).get, nums))


solution = Solution()

print([5, 4, 3, 2, 1].index(5))
print(solution.findRelativeRanks([5, 4, 3, 2, 1]))
