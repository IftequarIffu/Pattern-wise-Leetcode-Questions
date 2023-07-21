# Problem Link: https://leetcode.com/problems/dungeon-game/description/
# YT Video Link: https://www.youtube.com/watch?v=bya4Vow1Eq8

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        m=len(dungeon)
        n=len(dungeon[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        dp[m-1][n-1] =  (-1*dungeon[m-1][n-1]+1) if dungeon[m-1][n-1] <=0 else 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if(i==m-1 and j==n-1):
                    continue
                else:
                    if(i==m-1):
                        final=dp[i][j+1]
                        start=final-dungeon[i][j]
                        # print(start,final)
                        dp[i][j] = (start) if start>0 else 1
                    elif(j==n-1):
                        final=dp[i+1][j]
                        start=final-dungeon[i][j]
                        dp[i][j] = (start) if start>0 else 1
                    else:
                        final1=dp[i][j+1]
                        start1=final1-dungeon[i][j]
                        final2=dp[i+1][j]
                        start2=final2-dungeon[i][j]
                        dp[i][j] = min(start1,start2)
                        if(dp[i][j]>0):
                            dp[i][j]=dp[i][j]
                        else:
                            dp[i][j]=1
        if(dp[0][0]==0):
            return 1
        else:
            return dp[0][0]
