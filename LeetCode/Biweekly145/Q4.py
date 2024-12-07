class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        
        N = threshold + 1

        tmp = [el for el in nums if el <= threshold]
        res = len(nums) - len(tmp)
        nums = tmp

        parents = [i for i in range(N)]

        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]
        
        def uunion(x, y):
            root_x, root_y = ufind(x), ufind(y)
            if root_x != root_y:
                parents[root_y] = root_x

        for num in nums:
            i = 2
            multiple = num * i
            while multiple <= threshold:
                uunion(num, multiple)
                i += 1
                multiple = num * i

        res_set = set()
        for el in nums:
            res_set.add(ufind(el))
        return len(res_set) + res