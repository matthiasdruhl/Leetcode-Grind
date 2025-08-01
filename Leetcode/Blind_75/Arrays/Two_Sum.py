class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        inputs:
            - nums: a list of integers
            - target: integer we are looking to add to 
        outputs:
            - array containing i and j
                - indices that correspond to the numbers we are looking for
        constraints:
            - we know i and j exist
            - return smallest index first
        
        approach:
            - Use hashmap to store values and corresponding indexes
            - Iterate over nums
            - subtract nums from target 
            - see if this number is in hashmap already
                - if yes:
                    return array with i and j
                - else:
                    add index and number to hashmap and continue on
        
        time complexity - O(n)
            - Iterating over nums if O(n)
        """
        seen = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in seen:
                return [seen[pair], i]
            seen[nums[i]] = i