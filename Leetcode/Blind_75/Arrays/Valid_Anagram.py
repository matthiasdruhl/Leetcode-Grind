class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Anagram = string that contains exact same characters

        inputs
            - s: string
            - t: string
        output
            - boolean
                - True - if anagram
                - False - if not anagram
        Clarifying questions:
            - Will strings be same length

        approach:
            - Use array of buckets since alphabet has fixed size
                - Better memory then hashmap
                    - Double check this
            - iterate over both strings at same time
            - for char in s add 1 to corresponding bucket
            - for char in t subtract 1 from corresponding bucket
            - check if all buckets == 0 at the end

        time complexity - O(n)
            - Iterating over s and t is O(n) 
            - Iterating over buckets is O(1) since len buckets is fixed (26)
        """
        
        # could just use Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
        buckets = [0] * 26
        for i in range(len(s)):
            buckets[ord(s[i]) - ord("a")] += 1
        for i in range(len(t)):
            if buckets[ord(t[i]) - ord("a")] <= 0:
                return False
            buckets[ord(t[i]) - ord("a")] -= 1
            
        for bucket in buckets:
            if bucket != 0:
                return False
        return True