### Link: https://leetcode.com/problems/relocate-marbles/

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        
        d={}
        
        for i in nums:
            d[i]=True
        
        for i in range(len(moveFrom)):
            if(d[moveFrom[i]]==1):
                d[moveFrom[i]]=False
                d[moveTo[i]]=True
        
        ans=[]
        for i in d:
            if(d[i]==True):
                ans.append(i)
        
        return sorted(ans)
