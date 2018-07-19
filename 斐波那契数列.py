"""
斐波那契数据当前一项是前两项之和
"""


class Solution:
    def Fibonacci(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


solution = Solution()
result = solution.Fibonacci(5)
print(result)