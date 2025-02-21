def get_res(number, amount_of_powers_needed):
    if number <= 0:
        return float('-inf')
    highest_power = number.bit_length() - 1
    highest_power_val = 2 ** highest_power
    if amount_of_powers_needed == 1:
        return highest_power_val
    
    res_taking = highest_power_val + get_res(number - highest_power_val, amount_of_powers_needed - 1)
    
    res_not_taking = 0
    for power_shift in range(1, amount_of_powers_needed + 1):
        cur_power = highest_power - power_shift
        if cur_power < 0:
            res_not_taking = float('-inf')
            break
        res_not_taking += 2 ** cur_power
    return max(res_taking, res_not_taking)

n = int(input())
for _ in range(n):
    a = int(input())
    if a < 7:
        print(-1)
        continue
    res = get_res(a, 3)
    print(res)

