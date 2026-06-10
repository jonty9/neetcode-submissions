class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
    
        left, right = 0,0
        cHash = {}
        maxSub = 0
        for i in s:
            if s[right] in cHash and cHash[s[right]] >= left:
                left = cHash[s[right]]+1
                print("Doesn't exists", s[right])
            cHash[s[right]] = right
            print("Left and right", left, right, cHash)
            right+=1

            length = right - left
            print("Length - ",length, maxSub)
            if maxSub < length:
                maxSub = length
        
        return maxSub