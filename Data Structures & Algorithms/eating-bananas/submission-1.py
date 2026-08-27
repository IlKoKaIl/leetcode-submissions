import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = max(piles)
        res = float('inf')


        while left <= right:
            cur_speed = ((left + right) // 2)
            eat_time = 0
            for pile in piles:
                eat_time += math.ceil(pile/cur_speed)
            
            if eat_time > h: #if eating too slow
                left = cur_speed + 1

            elif eat_time <= h: #can eat slower
                right = cur_speed - 1
                res = min(res, cur_speed)
                
        
        return res

            


        

        