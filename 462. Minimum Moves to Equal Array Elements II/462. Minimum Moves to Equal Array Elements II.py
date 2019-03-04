# 方法一、找到中位数,并计算所有数与中位数的差值
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = 0
        n = len(nums)
        nums.sort()
        # 求出中位数
        mid = (nums[(n + 1) // 2 - 1] + nums[-n // 2]) // 2

        for i in nums:
            steps += abs(mid - i)

        return steps

#方法二、进阶,比中位数小的要加到中位数,比中位数大的要减到中位数,所以可以转化为大数与小数的差

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = 0
        nums.sort()
        i = 0
        j = len(nums) - 1
        # 利用大数和小数共同达到中位数产生的差,加快循环
        while i < j:
            steps += nums[j] - nums[i]
            j -= 1
            i += 1

        return steps