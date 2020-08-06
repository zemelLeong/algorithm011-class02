class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans, length = 0, len(s)
        if length == 0: return 0
        dp = [0] * length
        for i in range(1, length):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 1] + 2
                    if i - 2 >= 0: dp[i] += dp[i - 2]
                elif (i - dp[i - 1] - 1) >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2
                    if (i - dp[i - 1] - 2) >= 0: dp[i] += dp[i - dp[i - 1] - 2]
                ans = ans if dp[i] < ans else dp[i]
        return ans