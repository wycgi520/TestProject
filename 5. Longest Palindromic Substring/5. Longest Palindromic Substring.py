# 方法一、中间扩展法, 每判断到一个字符, 便以其为中心扩展寻找回文
class Solution(object):
    def expand(self, str, L, R):
        while (L >= 0 and R < len(str)) and str[L] == str[R]:
            L -= 1
            R += 1
        return R - L - 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        len_p = temp_1 = temp_2 = 1
        start = end = 0

        if n in (0, 1):
            return s

        for i in range(n):

            temp_1 = self.expand(s, i, i)

            if i > 0 and s[i] == s[i - 1]:
                temp_2 = self.expand(s, i - 1, i)

            temp = max(temp_1, temp_2)
            if temp > len_p:
                len_p = temp
                start = i - temp / 2
                end = i + (temp - 1) / 2

        return s[start:end + 1]
