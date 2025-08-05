class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Anagram is a string that contains exact same characters as another string

        Inputs: 
            strs: Array of strings
        Outputs:
            - 2d array where all anagrams are grouped in individual arrays
        
        approach:
            - Use hashmap (default_dict of list)  to store bucket counts for each string
            - iterate over all strings and get bucket counts
            - convert buckets to tuples and store in hashmap
                - tuple bucket is the key and str is the value
                - if bucket already exists we can just apppend onto the str

        time_complexity = n * m
            - n is number of words
            - m is lenght of longest word
        """
        grouped_anagrams = defaultdict(list)
        for word in strs:
            buckets = [0] * 26
            for i in word:
                buckets[ord(i)- ord("a")] += 1
            grouped_anagrams[tuple(buckets)].append(word)
        return list(grouped_anagrams.values())