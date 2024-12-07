class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        prefix_sums = [0] * (len(nums) + 1)
        res = float('inf')
        for i in range(len(nums)):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        n = len(nums)
        for start in range(n):
            minimum_end = start + l
            if minimum_end > n:
                break
            maximum_end = min(start + r, n)
            for end in range(minimum_end, maximum_end + 1):
                current_sum = prefix_sums[end] - prefix_sums[start]
                if current_sum > 0:
                    res = min(res, current_sum)
        if res == float('inf'):
            return -1
        return res
