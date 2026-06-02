class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashofhash = {}
        for i,n in enumerate(strs):
            stringHash = [0]*26
            for j in n:
                stringHash[ord(j) - ord('a')]+=1
            tupleofHashtable = tuple(stringHash)
            if tupleofHashtable in hashofhash:
                hashofhash[tupleofHashtable].append(n)
            else:
                hashofhash[tupleofHashtable] = [n]

        return [values for values in hashofhash.values()]