class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        inputs:
            - nums: integer array
            - k: integer

        ouputs: 
            - k most frequent elements from nums

        approach:
            - Use counter to count elements
            - use buckets to keep track of the most used elements (Could be a lot of buckets)
            - Iterate over buckets backwards and append to an array until len array == k
            - return array
        
        Time complexity - O(n):
            - Counting elements O(n)
            - Iterating over counter is O(n)
            - itertaing over buckets is O(n)
        """

        count = Counter(nums)
        print (count)
        buckets = [[] for i in range(len(nums) + 1)]
        for num, c in count.items():
            buckets[c].append(num)
        
        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

