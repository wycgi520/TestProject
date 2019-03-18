#方法一、找出规律,具体规律请参见说明文档
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        # 建立图
        self.g = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            self.g[x][y] = v
            self.g[y][x] = 1.0 / v

        # 如果x和y都在图中,那么就可能有答案,若否,则没有答案
        ans = [self.divide(x, y, set()) if x in self.g and y in self.g else -1.0 for x, y in queries]
        return ans

    # 深度优先搜索,找到可以连通的图
    def divide(self, x, y, visited):
        if x == y: return 1.0
        visited.add(x)
        # 循环x节点下的每一个节点,如果这个节点已经在路径中遍历过了, 则不同重复遍历, 通过递归返回后面节点的乘积
        # 递归到最后, 如果存在匹配的图的终点, 那么i就等于y,在下一次递归时会出现x==y, 然后返回1
        for i in self.g[x]:
            if i in visited: continue
            d = self.divide(i, y, visited)
            if d > 0: return d * self.g[x][i]
        return -1.0

# 方法二, 并查集(待补充)