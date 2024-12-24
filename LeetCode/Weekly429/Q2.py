class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = [nums[0] - k]
        def min_to_add_to_be_larger(el, cur):
            l, r = -k, k
            res = None
            while l <= r:
                p = (l + r) // 2
                if cur + p > el:
                    res = p
                    r = p - 1
                else:
                    l = p + 1
            return res
        
        for i in range(1, len(nums)):
            x = min_to_add_to_be_larger(res[-1], nums[i])
            if x is None:
                continue
            if -k <= x <= k:
                res.append(nums[i] + x)
        #print(res)
        return len(res)
            