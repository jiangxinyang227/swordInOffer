"""
思路： 用二分法进行查找
"""

class Solution:

    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0

        start = 0
        end = len(rotateArray) - 1

        while rotateArray[start] >= rotateArray[end]:
            if end - start == 1:
                return rotateArray[end]

            midIndex = (start + end) // 2
            if rotateArray[start] == rotateArray[midIndex] == rotateArray[end]:
                return rotateArray[midIndex]

            elif rotateArray[midIndex] >= rotateArray[start]:
                start = midIndex

            elif rotateArray[midIndex] <= rotateArray[end]:
                end = midIndex
        return rotateArray[0]


if __name__ == '__main__':
    solution = Solution()
    array = []
    result = solution.minNumberInRotateArray(array)
    print(result)