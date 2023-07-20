Problem Link: https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n=len(matrix)
        dp=[[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if(i==0):
                    dp[i][j]=matrix[i][j]
                else:
                    if(j-1<0):
                        l=float('inf')
                    else:
                        l=dp[i-1][j-1]
                    
                    curr=dp[i-1][j]
                    
                    if(j+1>=n):
                        r=float('inf')
                    else:
                        r=dp[i-1][j+1]
                    
                    temp=min(min(l,r),curr)
                    dp[i][j]=temp+matrix[i][j]
        return min(dp[n-1])
