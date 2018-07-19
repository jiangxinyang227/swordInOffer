"""
思路：归纳法
台阶数 跳法
1       1
2       2
3       4
4       8
"""


class Solution:
    def jumpFloorII(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        n = 1
        for i in range(number - 1):
            n *= 2

        return n


if __name__ == '__main__':
    solution = Solution()
    result = solution.jumpFloorII(4)
    print(result)
