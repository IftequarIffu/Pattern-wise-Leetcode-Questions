Problem Link: https://leetcode.com/problems/maximal-square/description/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        dp=[[-1 for i in range(cols)] for j in range(rows)]
        
        def recursion(i,j):

            if(i>=rows or j>=cols):
                return 0

            if(dp[i][j]==-1):
                
                # Run these recursions even if matrix[i][j]==0
                # Because, it is used to continue recursion 
                # throughout the matrix
                right=recursion(i,j+1)
                down=recursion(i+1,j)
                diagonal=recursion(i+1,j+1)

                if(matrix[i][j]=="0"):
                    dp[i][j]=0
                else:
                    dp[i][j]=min(right,down,diagonal)+1

            # Calculating max   
            self.ans=max(self.ans,dp[i][j])
            return dp[i][j]
        self.ans=0
        recursion(0,0)
        print(dp)
        return self.ans**2
