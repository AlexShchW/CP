class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        nums = sorted(set(nums))
        res = len(nums)
        
        if nums[0] == k:
            res -= 1
        return res