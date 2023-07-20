Problem Link: https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:

        def isPrime(x):
            for i in range(2,int(x**(0.5))+1):
                if(x%i==0):
                    return False
            return True


        dp=[0 for i in range(n+1)]
        dp[0]=0
        dp[1]=0
        for i in range(2,n+1):
            if(isPrime(i)):
                dp[i]=i
            else:
                for j in range(i-1,-1,-1):
                    if(i%j==0):
                        dp[i]=dp[j]+(i//j)
                        break
        return dp[n]
