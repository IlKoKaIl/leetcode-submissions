class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0, len(heights) -1 
        max_area = 0
        
        while p1 < p2:
            cur_area = (min(heights[p2], heights[p1]) * (p2-p1))
            max_area = max(max_area, cur_area)

            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        
        return max_area



