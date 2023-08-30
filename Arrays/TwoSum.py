# Bruteforce : O(N²) time and O(1) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        length=len(nums)
        for idx1 in range(n-1):
            for idx2 in range(idx1+1,length):
                if(nums[idx1]+nums[idx2]==target):
                    return [idx1,idx2]
                  

# Using dictionary: O(N) time and O(N) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   
        dictionary={}
        for idx in range(len(nums)):
            if(target-nums[idx] in dictionary):
                return [idx,dictionary[target-nums[idx]]]
            dictionary[nums[i]]=i

