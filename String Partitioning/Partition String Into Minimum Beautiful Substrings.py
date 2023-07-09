### Link: https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        
        def isValid(s):

            # String must not have leading zeros
            if(s[0]=='0'):
                return False


            # Converting string to decimal
            ans=0
            for i in range(len(s)-1,-1,-1):
                if(s[i]=='1'):
                    ans=ans+2**(len(s)-i-1)

            # Check if decimal is a power of 5
            while(True):
                if(ans==1):
                    break
                if(ans%5!=0):
                    return False
                else:
                    ans=ans/5
            
            return True
            
              
        def recursion(s):
            
            if(len(s)==0):
                return 0
            
            ans=20
            for i in range(len(s)):
                firstString=s[:i+1]
                secondString=s[i+1:]
                if(isValid(firstString)):
                    ans = min(ans,recursion(secondString)+1)
            
            return ans
            
        # print(isPowerOf5('1011'))
        if(recursion(s)==20):
            return -1
        return recursion(s) 
