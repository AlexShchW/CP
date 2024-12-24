class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = collections.deque(nums)
        ops = 0
        while nums:
            if len(nums) == len(set(nums)):
                return ops
            ops += 1
            if nums:
                nums.popleft()
            if nums:
                nums.popleft()
            if nums:
                nums.popleft()
        return ops