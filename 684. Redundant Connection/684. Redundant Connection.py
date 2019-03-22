# 方法一、用字典g构建图,然后用深度优先搜索的方法遍历图,
# 遍历图的时候, 把已经遍历过的胡同都删掉, 这样保证遍历路径是相连通的
# 当遍历到环节点的时候, 就可以把环返回出来
# 最后找这个环的一条边, 这条边相对于其他边来说, 位于原来输入的二维数组edges中最远
class Solution(object):
    def __init__(self):
        self.isSolve = False
        self.lines = list()

    def _conti(self, m, visited):
        visited.append(m)
        for n in self.g[m]:
            if self.isSolve: return
            if n in visited:
                if n == visited[-2]: continue
                index_n = visited.index(n)
                self.lines = visited[index_n:]+[n]
                self.isSolve = True
            self._conti(n, visited)
        visited.pop()

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        import collections

        self.g = collections.defaultdict(list)
        lines_sort = list()

        for m, n in edges:
            self.g[m].append(n)
            self.g[n].append(m)

        self._conti(edges[0][0], list())

        lines_len = len(self.lines)
        for i in range(lines_len-1):
            if self.lines[i] > self.lines[i+1]:
                line = [self.lines[i+1], self.lines[i]]
            else:
                line = [self.lines[i],self.lines[i+1]]
            lines_sort.append(edges.index(line))

        max_index = max(lines_sort)
        return edges[max_index]