class Solution:
    def smallestNumber(self, n: int) -> int:
        b = list(bin(n)[2:])
        res = '1' * len(b)
        return int(res, 2)