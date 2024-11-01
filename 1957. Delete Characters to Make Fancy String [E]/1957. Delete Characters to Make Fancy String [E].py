class Solution:
    def makeFancyString(self, s: str) -> str:
        check_letter = s[0]
        frequency = 1
        answer = s[0]

        for i in range(1, len(s)):
            if s[i] == check_letter:
                frequency += 1
            else:
                check_letter = s[i]
                frequency = 1

            if frequency < 3:
                answer += s[i]

        return answer

# test
solution = Solution()
print(solution.makeFancyString("leeetcode"))
print(solution.makeFancyString("aaabaaaa"))
print(solution.makeFancyString("aab"))