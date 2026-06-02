class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charList = [0]*26

        for i in range(len(s)):
            charList[ord(s[i]) - ord('a')]+=1
            charList[ord(t[i]) - ord('a')]-=1
        for i in charList:
            if i != 0:
                return False
        return True
