### Link: https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        dp=[0]*(n)
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if(abs(nums[i]-nums[j])<=target):
                    if(j==n-1):
                        dp[i]=max(dp[i],1)
                    else:
                        if(dp[j]!=0):
                            dp[i]=max(dp[i],dp[j]+1)
                          
        if(dp[0]==0):
            return -1
        else:
            return dp[0]
