#方法一、构建并查集,循环将数加入子集中,最后判断最大的子集的长度
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        Union = dict()
        # depth = dict()
        out = 0

        for i in nums:

            if i in Union:
                continue
            elif i - 1 in Union:
                Union[i] = i - 1
                if i + 1 in Union:
                    Union[i + 1] = i
            elif i + 1 in Union:
                Union[i + 1] = i
                Union[i] = i
                if i - 1 in Union:
                    Union[i] = i - 1
            else:
                Union[i] = i

        for i in nums:
            n = 1
            while i != Union[i]:
                i = Union[i]
                n += 1
            out = max(out, n)
        return out

#方法二\ 层级小的树合并到层级高的树中, 减少递归次数(用rank来保存层级)
class Solution(object):
    def get_root(self, i):
        if i != self.Union[i]:
            i = self.get_root(self.Union[i])
        return i

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        self.Union = dict()
        count = dict()
        rank = dict()

        for i in nums:
            if i in self.Union:
                continue
            elif i - 1 in self.Union:
                j_root = self.get_root(i - 1)
                j_rank = rank[j_root]
                self.Union[i] = j_root
                count[j_root] += 1
                if j_rank == 1:
                    rank[j_root] = 2
                if i + 1 in self.Union:
                    k_root = self.get_root(i + 1)
                    if rank[k_root] == rank[j_root]:
                        self.Union[j_root] = k_root
                        count[k_root] += count[j_root]
                        rank[k_root] += 1
                    elif rank[k_root] > rank[j_root]:
                        self.Union[j_root] = k_root
                        count[k_root] += count[j_root]
                    else:
                        self.Union[k_root] = j_root
                        count[j_root] += count[k_root]
            elif i + 1 in self.Union:
                m_root = self.get_root(i + 1)
                m_rank = rank[m_root]
                if m_rank == 1:
                    rank[m_root] = 2
                self.Union[i] = m_root
                count[m_root] += 1
            else:
                self.Union[i] = i
                count[i] = 1
                rank[i] = 1

        return max(count.values()) if nums else 0