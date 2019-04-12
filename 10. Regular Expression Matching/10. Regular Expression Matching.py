# 方法一. 递归, 如果首字母匹配,则匹配下一个,如果有*, 则分情况匹配
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        in_str = s
        pt = p

        if not pt:
            return not in_str

        first_match = bool(in_str) and pt[0] in {in_str[0], '.'}

        if len(pt) >= 2 and pt[1] == '*':
            # 一种情况是*号一个都没有匹配到原字符串, 然后or另一种情况是*匹配到原字符串
            return (self.isMatch(in_str, pt[2:])
                    or first_match and self.isMatch(in_str[1:], pt))
        else:
            # 没有*号, 直接跳到下一个
            return first_match and self.isMatch(in_str[1:], pt[1:])


# 方法二. 动态规划
class Solution(object):
    def isMatch(self, s, p):
        """ :type s: str :type p: str :rtype: bool """
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        # 先构造s字符串为空, 但p匹配中有*的情况
        for j in range(2,len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1,len(s) + 1):
            for j in range(1,len(p) + 1):
                # 如果有*号,如果*号只匹配了s中的一个,那么dp[i][j-1]为真, 如果*号没有匹配s的字符串,那么dp[i][j-2]为真
                # 如果*号匹配了s中的多个字符串,又可以分为两种情况, 1. 如果*号前的字符跟s最后的字符匹配,或者为"."
                # 则明显,即使s中去掉最后一个字符(因为匹配多个,至少一个, 所以只能去掉最后一个,不能去掉两个), 也能跟p匹配
                # 也即 dp[i-1][j]为真
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                # 正常情况下, 如果直接匹配, 则与dp[i-1][j-1]相同
                elif p[j-1] == '.' or s[i-1] == p[j - 1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[len(s)][len(p)]