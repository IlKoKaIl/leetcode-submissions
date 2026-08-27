class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_f = 0
        res = 0

        for right in range(len(s)):
            c = s[right]
            count[c] = (count.get(c, 0) + 1)

            max_f = max(max_f, count[c])

            size = right - left + 1

            while size - max_f > k:
                old = s[left]
                count[old] -= 1
                
                left += 1
                size = right - left + 1
            
            res = max(res, size)
        
        return res

        