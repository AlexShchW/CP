res = 0

def f(a_x, a_y, b_x, b_y, p_x, p_y):

    storage = {}
    def ff(a_pressed, b_pressed, cur_x, cur_y):
        if cur_x == p_x and cur_y == p_y:
            return 0
        if a_pressed > 100:
            return float('inf')
        if b_pressed > 100:
            return float('inf')
        if cur_x > p_x or cur_y > p_y:
            return float('inf')
        if (a_pressed, b_pressed, cur_x, cur_y) in storage:
            return storage[(a_pressed, b_pressed, cur_x, cur_y)]
        
        res = min((3 + ff(a_pressed + 1, b_pressed, cur_x + a_x, cur_y + a_y)), 1 + ff(a_pressed, b_pressed + 1, cur_x + b_x, cur_y + b_y))
        storage[(a_pressed, b_pressed, cur_x, cur_y)] = res
        return res
    
    res = ff(0, 0, 0, 0)
    if res == float('inf'):
        return 0, -1
    else:
        return 1, res

while True:
    try:
        line1 = input()
        if line1 == '':
            continue
        arr = line1.split(':')[1]
        arr = arr.split(',')
        x_arr = arr[0]
        y_arr = arr[1]
        x_val = x_arr.split('+')[1]
        y_val = y_arr.split('+')[1]
        a_x, a_y = int(x_val), int(y_val)

        line1 = input()
        arr = line1.split(':')[1]
        arr = arr.split(',')
        x_arr = arr[0]
        y_arr = arr[1]
        x_val = x_arr.split('+')[1]
        y_val = y_arr.split('+')[1]
        b_x, b_y = int(x_val), int(y_val)

        line1 = input()
        arr = line1.split(':')[1]
        arr = arr.split(',')
        x_arr = arr[0]
        y_arr = arr[1]
        x_val = x_arr.split('=')[1]
        y_val = y_arr.split('=')[1]
        p_x, p_y = int(x_val), int(y_val)

        code, cur_res = f(a_x, a_y, b_x, b_y, p_x, p_y)
        if code:
            res += cur_res


        
    except EOFError:
        break

print(res)