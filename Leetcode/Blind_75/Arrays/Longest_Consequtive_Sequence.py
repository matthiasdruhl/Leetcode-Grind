class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert array to a set for O(1) lookups
        # Iterate through set and for each numeber, check if the number - 1 is in set
        # If not, increment number and check if that new number is in set
        # Return longest consequtive of the sequences found
        seen = set(nums)
        longest_consequtive = 0
        for num in seen:
            if num - 1 not in seen:
                curr_length = 1
                while num + 1 in seen:
                    curr_length += 1
                    num += 1
                longest_consequtive = max(longest_consequtive, curr_length)
        return longest_consequtive