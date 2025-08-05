class Solution:
    # Iterate over the array and add the length plus a marker to the beginning
    # The length is to know how many characters
    # The marker is to know when the length ends (for multi digit arrays)
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        print("encoded_string: " + encoded)
        return encoded
    
    # Have 2 pointers
    # One iterates until it find the marker
    # The splice of the array that consists of the 2 strings will be the lenght
    # Add the splice from the marker + the length to the decoded array
    def decode(self, s: str) -> List[str]:
        decoded = []
        l = 0
        r = 0
        while l < len(s):
            while s[r] != "#":
                r += 1
            print(s[l:r])
            length = int(s[l:r])
            l = r + 1
            r = l + length
            decoded.append(s[l:r])
            l = r
        return decoded
           

        