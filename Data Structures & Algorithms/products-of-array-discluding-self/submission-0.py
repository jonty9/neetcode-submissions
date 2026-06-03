class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1]*len(nums)
        prefixProducts = [nums[0]]
        for i in range(1, len(nums)):
            prefixProducts.append(nums[i]*prefixProducts[i-1])
        # print(prefixProducts)

        sol[-1] = prefixProducts[-2]
        for i in range(len(nums)-2, -1, -1):
            sol[i] = prefixProducts[i-1]*nums[i+1]
            nums[i] *= nums[i+1]
        sol[0] = nums[1]
        return sol
    
