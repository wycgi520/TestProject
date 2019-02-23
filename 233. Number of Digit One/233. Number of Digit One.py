# 方法一、暴力法,直接循环计算所有数字的1的数量
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = 0

        for i in range(1, n + 1):
            out += str(i).count('1')

        return out

#方法二、找出规律,递归判断,具体规律请参见说明文档
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 1: return 0
        if n < 10: return 1

        L = 1
        m = n
        while True:
            m /= 10
            L += 1
            if m < 10:
                break
        c = m  # n的最高位
        k = 10 ** (L - 1)  # 跟n同位数的10的多次方

        if c == 1:
            # 最高位的1的数量+0~999..的1的数量+100..~n中不计最高位的1的数量
            return n - k + 1 + self.countDigitOne(k - 1) + self.countDigitOne(n - k)
        else:
            # 最高位的1的数量+0~999..的1的数量乘以最高位c+c00~n中1的数量
            return k + c * self.countDigitOne(k - 1) + self.countDigitOne(n - c * k)