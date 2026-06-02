class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()
        for i in range(len(nums)):
            hashTable[nums[i]] = i
        
        for i in range(len(nums)):
            required = target - nums[i]
            if required in hashTable and hashTable[required] != i:
                return [i, hashTable[required]] 
        
