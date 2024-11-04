from tabnanny import check


class Solution:
    def compressedString(self, word: str) -> str:
        answer = ""
        j = 0
        n = len(word)
        for i in range(1, n):
            if word[i] != word[j] or (i - j) == 9:
                answer += str(i - j) + word[j]
                j = i
        # last run
        answer += str(n - j) + word[j]
        return answer

# test
solution = Solution()
print(solution.compressedString("abcde"))
print(solution.compressedString("aaaaaaaaaaaaaabb"))