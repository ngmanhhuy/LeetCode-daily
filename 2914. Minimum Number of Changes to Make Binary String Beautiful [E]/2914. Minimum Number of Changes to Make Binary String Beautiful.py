class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        i = 0
        for i in range(0, n - 1, 2):
            if s[i] != s[i + 1]:
                count += 1

        return count

# test
solution = Solution()
print(solution.minChanges("1001"))
print(solution.minChanges("10"))
print(solution.minChanges("0000"))
print(solution.minChanges("11000111"))