from helper import read_blocks
from helper import get_pos_numbers_from_line
from helper import get_words_from_line


blocks = read_blocks()

patterns = get_words_from_line(blocks[0][0])

def get_res(towel):

    N = len(towel)
    storage = [None] * N
    def dp(idx):
        if idx == N:
            return 1
        if storage[idx] is not None:
            return storage[idx]
        res = 0
        for pattern in patterns:
            if idx + len(pattern) <= N:
                if towel[idx : idx + len(pattern)] == pattern:
                    res += dp(idx + len(pattern))
        storage[idx] = res
        return res
    
    return dp(0)

res = 0

towels = blocks[1]
for towel in towels:
    res += get_res(towel)

print(res)