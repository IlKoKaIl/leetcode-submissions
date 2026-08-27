class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        seen = set()
        max_len = 0

        for p2 in range(len(s)):
            while s[p2] in seen:
                seen.remove(s[p1])
                p1 += 1
            
            seen.add(s[p2])
            max_len = max(max_len, p2-p1 + 1)

        return max_len

        


        