class Solution(object):
    """
    167. Two Sum II - Input array is sorted


    """

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            if s < target:
                l += 1
            if s > target:
                r -= 1

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in xrange(len(numbers)):
        #     l, r = i + 1, len(numbers) - 1
        #     rest = target - numbers[i]
        #     while l <= r:
        #         mid = l + (r - l) // 2
        #         if numbers[mid] == rest:
        #             return [mid + 1, r + 1]
        #         elif numbers[mid] < rest:
        #             l = mid + 1
        #         else:
        #             r = mid - 1

        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i


solution = Solution()
print(solution.twoSum([5, 25, 75], 100))
