# Problem Link: https://leetcode.com/problems/triangle/description/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n=len(triangle)
        dp=[[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(i+1):
                if(i==0):
                    dp[i][j]=triangle[i][j]
                else:
                    if(j==0):
                        dp[i][j]=triangle[i][j]+dp[i-1][j]
                    elif(i==j):
                        dp[i][j]=triangle[i][j]+dp[i-1][j-1]
                    else:
                        dp[i][j]=triangle[i][j]+min(dp[i-1][j],dp[i-1][j-1])
        
        ans=float('inf')
        for j in range(n):
            ans=min(ans,dp[n-1][j])
        return ans
