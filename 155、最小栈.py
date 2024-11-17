# 用列表来实现栈的建立，首先这里的最小栈的意思就是说要实现一般栈所有的pop，push，操作，还要额外完成top，和getmin的操作，一个是返回栈顶元素，一个是返回这个栈中的最小值
class MinStack:
    def __init__(self):
        self.stack = []  #这个是主栈
        self.min_stack = []  # 辅助栈，用来存放栈的最小值

    def push(self,val):   #val 是要推进去的元素
        self.stack.append(val)  # 用列表的append方法实现stack的push方法
        if not self.min_stack or val <= self.min_stack[-1]:   #第一个限制条件是为了针对第一个元素进入辅助栈，而后面的限制条件是确保，最小值永远位于栈顶
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            res = self.stack[-1]
            self.stack.pop()
            if res == self.min_stack[-1]:
                self.min_stack.pop()


    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]

