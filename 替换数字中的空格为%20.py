

class Solution:

    def replaceSpace(self, s):

        s = list(s)
        count = len(s)
        for i in range(0, count):
            if s[i] == " ":
                s[i] = "%20"
        return "".join(s)


if __name__ == '__main__':

    solution = Solution()
    string = " "
    result = solution.replaceSpace(string)
    print(result)
