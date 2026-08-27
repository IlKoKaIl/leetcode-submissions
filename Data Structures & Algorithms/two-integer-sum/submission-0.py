class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}

        for i, val in enumerate(nums):
            dif = target - val
            if dif in value_index:
                return [value_index[dif], i]
            value_index[val] = i
            
            

        