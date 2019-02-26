# 方法一、先按成本排序,将可执行的项目按照利润排序,每次取最高利润即可
class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        import heapq

        heap = list()
        i = 0

        # 构建包括Profits和Capital的列表
        Projects = list(zip(Profits, Capital))

        # 将Projects列表按Capital排序
        Projects.sort(key=lambda x: x[1])

        # 按需要完成的项目数循环执行任务
        for _ in range(k):
            # 将可执行的任务的Profits压入堆中
            len_p = len(Projects)
            while i < len_p and Projects[i][1] <= W:
                heapq.heappush(heap, -Projects[i][0])
                i += 1

            # 取出heap中最大的Profits(取负数压进堆里,所以堆弹出的最小即最大)
            if heap != []:
                W -= heapq.heappop(heap)

        return W

# 方法一、优化排序,用了两个优先队列
class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        import heapq

        heap = list()

        # 构建包括Profits和Capital的列表
        Projects = list(zip(Capital, Profits))

        # 将Projects列表按Capital进行优先级排序
        heapq.heapify(Projects)

        # 按需要完成的项目数循环执行任务
        for _ in range(k):
            # 将可执行的任务的Profits压入堆中
            while Projects != [] and Projects[0][0] <= W:
                P_P = heapq.heappop(Projects)
                heapq.heappush(heap, -P_P[1])

            # 取出heap中最大的Profits(取负数压进堆里,所以堆弹出的最小即最大)
            if heap != []:
                W -= heapq.heappop(heap)

        return W
