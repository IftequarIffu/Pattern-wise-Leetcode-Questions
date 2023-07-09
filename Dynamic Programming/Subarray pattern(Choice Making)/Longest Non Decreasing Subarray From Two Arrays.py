### https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n=len(nums1)
        dp=[[1 for i in range(2)] for j in range(n)]
        ans=1
        for i in range(1,n):
            if(nums1[i-1]<=nums1[i]):
                dp[i][0]=max(dp[i][0],dp[i-1][0]+1)
            if(nums2[i-1]<=nums1[i]):
                dp[i][0]=max(dp[i][0],dp[i-1][1]+1)
            if(nums1[i-1]<=nums2[i]):
                dp[i][1]=max(dp[i][1],dp[i-1][0]+1)
            if(nums2[i-1]<=nums2[i]):
                dp[i][1]=max(dp[i][1],dp[i-1][1]+1)
                
        for i in range(n):
            for j in range(2):
                ans=max(ans,dp[i][j])
        
        return ans
