res = 0

def f(a_x, a_y, b_x, b_y, p_x, p_y):

    if (p_x * b_y - p_y * b_x) % (b_y * a_x - a_y * b_x) != 0:
        return -1
    
    a = (p_x * b_y - p_y * b_x) // (b_y * a_x - a_y * b_x)

    if (p_x - a * a_x) % b_x != 0:
        return -1
    
    b = (p_x - a * a_x) // b_x 

    return a * 3 + b

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
        p_x, p_y = int(x_val) + 10000000000000, int(y_val) + 10000000000000

        cur_res = f(a_x, a_y, b_x, b_y, p_x, p_y)
        if cur_res != -1:
            res += cur_res


        
    except EOFError:
        break

print(res)