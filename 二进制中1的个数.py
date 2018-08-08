"""
思路：二进制表示中，最后的那个1被减去后，低位都变为0，高位不变，按位与就可以去掉这个1
"""


class Solution:
    def NumberOf1(self, n):
        ret = 0
        while n:
            ret += 1
            n = n & n-1
        return ret