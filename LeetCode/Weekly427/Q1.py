class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [None] * N
        
        for i, el in enumerate(nums):
            if el == 0:
                result[i] = nums[i]
                continue
            if el > 0:
                new_idx = (i + el) % N
                result[i] = nums[new_idx]
            else:
                new_idx = (i - abs(el)) % N
                result[i] = nums[new_idx]
        return result