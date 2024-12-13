class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
                
        storage = {}
        storage[0] = 0
        res = float('-inf')

        cur_sum = 0
        cur_length = 0
        for i, el in enumerate(nums):
            cur_sum += el
            cur_length += 1
            lengths_of_ok = cur_length % k
            if lengths_of_ok not in storage:
                if lengths_of_ok >= k:
                    res = max(res, cur_sum)
                storage[lengths_of_ok] = cur_sum
            else:
                if lengths_of_ok >= k:
                    res = max(res, cur_sum)
                prev_val = storage[lengths_of_ok]
                res = max(res, cur_sum - prev_val)
                storage[lengths_of_ok] = min(storage[lengths_of_ok], cur_sum)
        
        return res