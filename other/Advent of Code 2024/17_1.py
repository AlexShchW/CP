from helper import read_blocks
from helper import get_pos_numbers_from_line

A = [0]
B = [0]
C = [0]
pointer = [0]

output = []

def get_comb(operand):
    if operand <= 3:
        return operand
    if operand == 4:
        return A[0]
    if operand == 5:
        return B[0]
    if operand == 6:
        return C[0]
    

# division
def op_0(operand):
    num = A[0]
    denum = 2 ** get_comb(operand)
    res = int(num / denum)
    A[0] = res
    pointer[0] += 2

# bitwise xor
def op_1(operand):
    res = B[0] ^ operand
    B[0] = res
    pointer[0] += 2

# last 3 bits
def op_2(operand):
    res = get_comb(operand) % 8
    B[0] = res
    pointer[0] += 2

# jnz
def op_3(operand):
    if A[0] == 0:
        pointer[0] += 2
        return
    pointer[0] = operand

# bxc
def op_4(operand):
    res = B[0] ^ C[0]
    B[0] = res 
    pointer[0] += 2


# out
def op_5(operand):
    tmp = get_comb(operand) % 8
    output.append(tmp)
    pointer[0] += 2

# bdv
def op_6(operand):
    num = A[0]
    denum = 2 ** get_comb(operand)
    res = int(num / denum)
    B[0] = res
    pointer[0] += 2

# cdv
def op_7(operand):
    num = A[0]
    denum = 2 ** get_comb(operand)
    res = int(num / denum)
    C[0] = res
    pointer[0] += 2


blocks = read_blocks()
A[0] = get_pos_numbers_from_line(blocks[0][0])[0]
B[0] = get_pos_numbers_from_line(blocks[0][1])[0]
C[0] = get_pos_numbers_from_line(blocks[0][2])[0]

commands = get_pos_numbers_from_line(blocks[1][0])

funcs_array = []
funcs_array.append(op_0)
funcs_array.append(op_1)
funcs_array.append(op_2)
funcs_array.append(op_3)
funcs_array.append(op_4)
funcs_array.append(op_5)
funcs_array.append(op_6)
funcs_array.append(op_7)

while pointer[0] < len(commands):
    cur_command, cur_operand = commands[pointer[0]], commands[pointer[0] + 1]
    funcs_array[cur_command](cur_operand)

print(','.join([str(el) for el in output]))