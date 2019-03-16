# 方法一、先用深度优先搜索算法把岛屿1转换成别的字符, 每当找到1时即改变整个岛屿, 然后往下找寻下一个岛屿,
# 直至整个遍历完全
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []: return 0
        m = len(grid)
        n = len(grid[0])
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        island = 0

        def _solve(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = ''
                for k in range(4):
                    _solve(i + d[k][0], j + d[k][1])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    _solve(i, j)
                    island += 1

        return island