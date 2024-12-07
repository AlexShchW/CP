class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        c = collections.Counter(nums)
        S = sum(nums)
        for el in nums:
            c[el] -= 1
            specials_and_sum = S - el
            if specials_and_sum % 2 != 0:
                c[el] += 1
                continue
            specials_sum = specials_and_sum // 2
            if c[specials_sum] > 0:
                return el
            c[el] += 1