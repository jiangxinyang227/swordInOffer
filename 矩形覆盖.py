"""
思路：归纳法，斐波那契数列的变种
n 方法数
1  1
2  2
3  3
4  5
"""


class Solution:
    def rectCover(self, number):
        a, b = 0, 1
        if number == 0:
            return a

        for i in range(number):
            a, b = b, a+b

        return b


if __name__ == '__main__':
    solution = Solution()
    result = solution.rectCover(2)
    print(result)