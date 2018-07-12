"""
解题思路，利用数组是有序的可以加速查询的效果
"""


class Solution:

    def Find(self, target, array):

        rows = len(array)
        columes = len(array[0])
        startRow = 0
        startCol = columes - 1

        while startRow < rows and startCol >= 0:
            print(startRow, startCol)
            if target == array[startRow][startCol]:
                return True
            if target < array[startRow][startCol]:
                startCol = startCol - 1

            if target > array[startRow][startCol]:
                startRow = startRow + 1

        return False


if __name__ == '__main__':

    solution = Solution()
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    target = 5
    result = solution.Find(target, array)
    print(result)