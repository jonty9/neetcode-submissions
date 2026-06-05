class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashTable = {}
        for i in nums:
            hashTable[i] = 0
        
        streak = 0
        for key in hashTable:
            if not (key - 1) in hashTable:
                tempcount = 1
                while (key + 1) in hashTable:
                    tempcount+=1
                    key+=1
                if streak < tempcount:
                    streak = tempcount
        
        return streak
        
        