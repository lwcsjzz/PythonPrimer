'''
Author: liuwenchang
Date: 2020-11-06 14:11:41
Description: https://github.com/lwcsjzz
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        dp = [[False]*n for _ in range(n)]
        for L in range(n):
            for i in range(n):
                j = i + L
                if j >= n:
                    break
                if L == 0:
                    dp[i][j] = True
                elif L == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and L+1 > len(s):
                    ans = s[i:j+1]
    return ans
