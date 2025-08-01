class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Input: 
        #     - Integer array (nums)
        # Output:
        #     - Boolean - 
        #    if any number appears multiple times - True 
        #    else False
        # Approach:
        #      - Utilize a set
        #      - Iterate over the array
        #      - Check if number has been seen by comparing to the array
        #      - If yes:
        #      -    Return True
        #      - Else:
        #      -    Add number to array and continue to next number

        seen = set() # Holds numbers we have seen:
        for num in nums:
            if num in seen: 
                return True
            else:
                seen.add(num)
        return False