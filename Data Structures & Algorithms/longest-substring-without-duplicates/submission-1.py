class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        res = 0
        
        for end in range(len(s)):
            # If the character is in seen AND its index is inside the current window
            if s[end] in seen and seen[s[end]] >= start:
                start = seen[s[end]] + 1
            
            # Always update the latest index of the character
            seen[s[end]] = end
            
            # Always update the maximum length found so far
            res = max(res, end - start + 1)
            
        return res