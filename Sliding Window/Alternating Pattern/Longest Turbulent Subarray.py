### Link: https://leetcode.com/problems/longest-turbulent-subarray/description/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        prev = ""
        n=len(arr)
        res=1
        i=1
        j=0
        while(i<n):

            if(arr[i-1]>arr[i] and prev!=">"):
                res=max(res,i-j+1)
                i+=1
                prev=">"
            
            elif(arr[i-1]<arr[i] and prev!="<"):
                res=max(res,i-j+1)
                i+=1
                prev="<"
            
            else:
                if(arr[i-1]==arr[i]):
                    i+=1
                    j=i-1
                else:
                    j=i-1
                prev=""
        return res
