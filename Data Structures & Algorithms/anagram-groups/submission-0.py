class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashofhash = {}
        for i,n in enumerate(strs):
            stringHash = [0]*26
            for j in n:
                stringHash[ord(j) - ord('a')]+=1
            if tuple(stringHash) in hashofhash:
                hashofhash[tuple(stringHash)].append(n)
            else:
                hashofhash[tuple(stringHash)] = [n]

        return [values for values in hashofhash.values()]