"""
思路： 一个栈保存正序列的数据，push数据到正序列，另一个栈保存反序列的数据，pop输出从反序列，但是两个栈中同时只能有一个栈中有数据
"""


class Solution:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        if self.stack2:
            for i in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
            self.stack1.append(node)
        else:
            self.stack1.append(node)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()

        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


if __name__ == '__main__':

    solution = Solution()
    solution.push(1)
    solution.push(2)
    solution.push(3)
    print(solution.pop())
    print(solution.pop())
    solution.push(4)
    print(solution.pop())
    solution.push(5)
    print(solution.pop())
    print(solution.pop())