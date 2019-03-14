#方法一、通过深度优先搜索把边界上的O以及与边界连通的O变成*, 最后遍历列表, 把O变成X,*变成O
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return None

        m, n = len(board), len(board[0])

        d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # 深度优先搜索
        def _solve(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = '*'
                for k in range(4):
                    _solve(i + d[k][0], j + d[k][1])

        # 取第一列和最后一列的边界点搜索连通点
        for i in range(m):
            _solve(i, 0)
            _solve(i, n - 1)

        # 取第一行和最后一行的边界点搜索连通点
        for j in range(n):
            _solve(0, j)
            _solve(m - 1, j)

        # 将所有O变为X, 所有*变为O
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'
