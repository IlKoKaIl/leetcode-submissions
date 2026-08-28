class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotating = just moving last num to front of array
        res = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            
            #either left -> mid sorted OR mid -> right sorted

            #range sorted
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])

            # left half sorted                
            if nums[left] <= nums[mid]:
                left = mid + 1

            #left half not sorted
            else:
                right = mid - 1

        return res




        