class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Iterate over the array and keep track of the product of all elements occurring before current index
        # Then iterate over the array in reverse and keep track of the product of all elements occurring after current index
        # Multiply the two products to get the final result for each index
        pre = [1] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = nums[i - 1] * pre[i - 1]
        
        post = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]
        
        for i in range(len(nums)):
            post[i] = pre[i] * post[i]
        return post        
    
        