# Problem Link: https://leetcode.com/problems/min-cost-climbing-stairs/description/
# Notes: Reaching top floor means reaching the nth index of the array.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n=len(cost)
        dp=[999999999]*(n)
        dp[n-1]=cost[n-1]
        dp[n-2]=cost[n-2]
        for i in range(n-3,-1,-1):
            dp[i]=cost[i]+min(dp[i+1],dp[i+2])
        print(dp)
        return min(dp[0],dp[1])
