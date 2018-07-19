"""
归纳法可知：
对应的就是一个斐波那契数列的变种形式
台阶数 跳法数
1       1
2       2
3       3
4       5
"""


class Solution:
    def jumpFloor(self, number):
        a, b = 0, 1
        if number == 0:
            return a
        for i in range(number):
            a, b = b, a+b

        return b


if __name__ == '__main__':
    solution = Solution()
    result = solution.jumpFloor(3)
    print(result)


