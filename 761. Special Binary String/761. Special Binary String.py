# 方法一、遍历字符串, 每找到匹配的特殊字符串, 便进行递归, 调用自身, 进行排序输出
# 最后将所有排序好的字符串输出即可(每个子字符串本身调用自己进行重新排序)
class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        cnt = i = 0
        v = list()

        for j, s in enumerate(S):
            cnt += 1 if s == "1" else -1
            if cnt == 0:
                if i + 1 != j:
                    v.append("1" + self.makeLargestSpecial(S[i + 1:j]) + "0")
                else:
                    v.append("10")
                i = j + 1

        v.sort(reverse=True)
        new_S = "".join(v)
        return new_S