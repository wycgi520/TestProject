# 方法一、求出递归公式
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            return 2*((n//2)+1-self.lastRemaining(n//2))

# 方法二、求出起始位置和终止位置,直至数字n为1(因为每次消除后,n都会减少一半,最终减少到1即结束)

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        S = 1
        interval = 1
        direction = True

        while n != 1:

            if direction:
                S = S - interval + 2 * interval * (n // 2)
            else:
                S = S + interval - 2 * interval * (n // 2)

            direction = not direction
            n = n // 2
            interval = 2 * interval

        return S