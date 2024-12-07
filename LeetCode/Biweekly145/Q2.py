class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:

        def get_res(perm):
            res = 0
            cur_factor = 1
            for el in perm:
                time_to_break = math.ceil(el / cur_factor)
                res += time_to_break
                cur_factor += K
        
            return res
        res = float('inf')
        for perm in itertools.permutations(strength):
            res = min(res, get_res(perm))
        return res
        