class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        seen = set()
        max_len = 0

    
        while p2 < len(s):
            if s[p2] not in seen:
                seen.add(s[p2])
                max_len = max(max_len, p2-p1 + 1)
                p2 += 1
            else:
                seen.remove(s[p1])
                p1 += 1
        
        return max_len
            

        


        