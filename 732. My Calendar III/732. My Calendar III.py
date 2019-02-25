#方法一、找出规律,具体规律请参见说明文档
class MyCalendarThree(object):

    def __init__(self):
        self.time_lists = list()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        # 将start标记为1,end标记为-1,并插入time_lists列表中
        self.time_lists += [[start, 1], [end, -1]]

        # 给列表排序(start和end的大小一起排序,上面1和-1的设置很重要,end的标记一定要小于start的标记)
        self.time_lists.sort()

        K = 0  # 最终返回的K值
        Part_K = 0  # 局部K值
        # 标记为1时累加1,标记为-1时减1,在累计和最大时更新K
        for _, symbol in self.time_lists:
            # 遇到start时,证明有交叉的日程安排,累加1
            # 当遇到end时,标记一个日程已经结束,不能再累计,应当减1
            Part_K += symbol

            K = max(Part_K, K)

        return K

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)