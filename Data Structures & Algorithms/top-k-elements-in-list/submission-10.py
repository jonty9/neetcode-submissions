class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else: 
                freq[i]+=1
        
        # print("freq: ", freq, bucket)
        for key, val in freq.items():
            bucket[val].append(key)
            print("After every bucket", bucket)
        
        # print("Bucket ", bucket)
        resp = []
        for i in bucket[::-1]:
            # print(i)
            for j in i:
                # print(j)
                resp.append(j)

                if len(resp) == k:
                    return resp
            
        