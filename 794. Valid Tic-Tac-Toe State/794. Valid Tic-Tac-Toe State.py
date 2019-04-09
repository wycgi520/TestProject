# 方法一、暴力法, 直接按照条件进行一步步判断
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """

        x_count = 0
        o_count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    x_count += 1
                elif board[i][j] == 'O':
                    o_count += 1

        if o_count < x_count - 1 or o_count > x_count: return False
        if o_count == x_count - 1 and self.Is_winned(board, 'O'): return False
        if o_count == x_count and self.Is_winned(board, 'X'): return False

        return True

    def Is_winned(self, board, letter):
        for j in range(3):
            if all([board[i][j] == letter for i in range(3)]): return True
            if all([board[j][i] == letter for i in range(3)]): return True
        if board[0][0] == board[1][1] == board[2][2] == letter: return True
        if board[0][2] == board[1][1] == board[2][0] == letter: return True
        return False
