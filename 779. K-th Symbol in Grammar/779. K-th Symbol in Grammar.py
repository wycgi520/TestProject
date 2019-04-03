# 方法一、暴力法, 直接递归替代所有字符串,超时
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """

        def generate_bytes(lines_num):
            if lines_num == 1:
                return "0"
            bytes_str = generate_bytes(lines_num - 1)
            temp_str = bytes_str.replace("0", "Z").replace("1", "O")
            new_str = temp_str.replace("Z", "01").replace("O", "10")
            print(new_str)
            return new_str

        string = generate_bytes(N)

        return string[K - 1]


# 方法2, 只需要构造一半的字符串, 有规律, 奇数时字符串是对称的, 且一边与上一行相同, 偶数时两边字符串相反
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """

        def generate_bytes(lines_num):
            if lines_num == 1:
                return "0"
            bytes_str = generate_bytes(lines_num - 1)
            new_str = ""
            if lines_num % 2:
                for s in bytes_str:
                    new_str = s+new_str
            else:
                for s in bytes_str:
                    reverse_s = "1" if s == "0" else "0"
                    new_str = reverse_s+new_str
            return bytes_str + new_str

        string = generate_bytes(N)

        return string[K - 1]


# 方法3, 根据K来选择N, 如果K较小, 那就不用弄那么多行, 因为每一行都是根据前一行可以得到的
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """

        import math

        def generate_bytes(lines_num):
            if lines_num == 1:
                return "0"
            bytes_str = generate_bytes(lines_num - 1)
            new_str = ""
            if lines_num % 2:
                for s in bytes_str:
                    new_str = s + new_str
            else:
                for s in bytes_str:
                    reverse_s = "1" if s == "0" else "0"
                    new_str = reverse_s + new_str
            return bytes_str + new_str

        New_N = math.ceil(math.log(K, 2)) + 1
        string = generate_bytes(New_N)

        return string[K - 1]

# 方法4, 因为每一行具有重复性, 所以可以只看K , 每次都对称获取K即可
import math


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """

        if K == 1:
            return 0
        new_N = math.ceil(math.log(K, 2)) + 1
        reverse_K = 2 ** (new_N - 1) - K + 1
        next_num = self.kthGrammar(new_N, reverse_K)
        if new_N % 2:
            return next_num
        else:
            return 0 if next_num else 1

# 方法5\ 通过画图可知, 下一行的K的值如果是奇数, 则等于上一行中(K+1)//2的值, 如果是偶数, 则与上一行中(K+1)//2的值相反
import math


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """

        if K == 1 and N == 1:
            return 0

        a = self.kthGrammar(N - 1, (K + 1) // 2)
        b = 0 if a else 1
        if K % 2:
            return a
        else:
            return b
