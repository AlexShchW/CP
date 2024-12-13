BLINKS = 75

storage = {}

def get_res(number, blinks_left):
    if not blinks_left:
        return 1
    if (number, blinks_left) in storage:
        return storage[(number, blinks_left)]
    s_number = str(number)
    if number == 0:
        res = get_res(1, blinks_left - 1)
    elif len(s_number) % 2 == 0:
        res = get_res(int(s_number[:len(s_number) // 2]), blinks_left - 1) + get_res(int(s_number[len(s_number) // 2:]), blinks_left - 1)
    else:
        res = get_res(number * 2024, blinks_left - 1)
    storage[(number, blinks_left)] = res
    return res

res = [get_res(int(el), BLINKS) for el in input().split()]
print(sum(res))