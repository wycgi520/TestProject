#方法一、使用深度优先搜索算法, 去掉所有找到的图的其他点, 只剩下一个头节点, 最后计算留下来的头结点的数量
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        students_out = [x for x in range(n)]

        def _solve(i, j, visited):
            if j in students_out:
                students_out.remove(j)
            else:
                return
            visited.add(i)
            for k in range(n):
                if k != j and (k not in visited) and M[j][k] == 1:
                    _solve(j, k, visited)

        index = 0
        m = n
        while index < m:
            i = students_out[index]
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    _solve(i, j, set())
            index += 1
            m = len(students_out)

        circle_friends = len(students_out)
        return circle_friends

#

