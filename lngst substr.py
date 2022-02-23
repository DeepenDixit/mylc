class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        rs = 0
        
        for j in range(1, len(s)+1):
            if len(set(s[i:j])) != j-i:
                rs = max(rs, j-i-1)
                i += 1
            elif j == len(s):
                rs = max(rs, j-i)
        
        return rs