# 方法一、 通过set无重复元素的特性和排序算法实现
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Set_nums = set(nums)
        Len_set = len(Set_nums)

        if Len_set < 3:
            return max(Set_nums)

        Arr_set = list(Set_nums)
        Arr_set.sort()
        return Arr_set[-3]

#方法二、通过三个数记录最大的三个数实现,时间复杂度为O(n)
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = [float("-inf")] * 3

        for i in nums:
            # 这里是为了不重复,所以判断已经有了的数字就跳过
            # 这样判断可能效率较低,实际上,可以通过and下面的判断式,同时判断有没有重复,进而提高效率
            if i in res:
                continue
            elif i > res[0]:
                res = [i, res[0], res[1]]
            elif i > res[1]:
                res = [res[0], i, res[1]]
            elif i > res[2]:
                res = [res[0], res[1], i]

        return res[2] if res[2] != float("-inf") else res[0]