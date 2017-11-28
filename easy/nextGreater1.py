# coding:utf-8
class Solution:
    """
    496. Next Greater Element I

    Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
    Output: [-1,3,-1]

    Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
    """

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # ans = []
        # for i in nums1:
        #     index = nums2.index(i)
        #     output = -1
        #     for j in nums2[index:]:
        #         if j > i:
        #             output = j
        #             break
        #     ans.append(output)
        # return ans

        # Use stack to find all
        # 1.循环nums2，先把当前值入栈
        # 2.查看后面的值，如果有大于栈里的值，字典表赋值，key：当前值 value:比他的值
        # 3.栈pop最上端的值
        d = {}
        stack = []
        for num in nums2:
            while stack:
                if num > stack[-1]:
                    d[stack.pop(-1)] = num
                else:
                    break
            stack.append(num)

        # Loop to find the result
        return [d[num] if num in d else -1 for num in nums1]


solution = Solution()
print(solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
