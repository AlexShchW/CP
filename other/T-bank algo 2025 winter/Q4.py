import math
n, x, y, z = [int(el) for el in input().split()]
arr = [int(el) for el in input().split()]

lcm_xy = math.lcm(x, y)
lcm_xz = math.lcm(x, z)
lcm_yz = math.lcm(y, z)
lcm_xyz = math.lcm(x, y, z)

x_costs = []
y_costs = []
z_costs = []
xy_costs = []
xz_costs = []
yz_costs = []
best_xyz_cost = float('inf')

def update_best_cost(costs_array, new_cost, new_index):
    if len(costs_array) < 3:
        costs_array.append((new_cost, new_index))
        costs_array.sort()
    else:
        if new_cost <= costs_array[0][0]:
            costs_array[2] = costs_array[1]
            costs_array[1] = costs_array[0]
            costs_array[0] = (new_cost, new_index)
        elif new_cost <= costs_array[1][0]:
            costs_array[2] = costs_array[1]
            costs_array[1] = (new_cost, new_index)
        elif new_cost < costs_array[2][0]:
            costs_array[2] = (new_cost, new_index)

for i, el in enumerate(arr):
    cost_x = (x - (el % x)) % x
    cost_y = (y - (el % y)) % y
    cost_z = (z - (el % z)) % z
    
    cost_xy = (lcm_xy - (el % lcm_xy)) % lcm_xy
    cost_xz = (lcm_xz - (el % lcm_xz)) % lcm_xz
    cost_yz = (lcm_yz - (el % lcm_yz)) % lcm_yz
    
    cost_xyz = (lcm_xyz - (el % lcm_xyz)) % lcm_xyz
    best_xyz_cost = min(best_xyz_cost, cost_xyz)
    
    update_best_cost(x_costs, cost_x, i)
    update_best_cost(y_costs, cost_y, i)
    update_best_cost(z_costs, cost_z, i)
    update_best_cost(xy_costs, cost_xy, i)
    update_best_cost(xz_costs, cost_xz, i)
    update_best_cost(yz_costs, cost_yz, i)

res = best_xyz_cost

for x_val, x_idx in x_costs:
    for y_val, y_idx in y_costs:
        for z_val, z_idx in z_costs:
            if x_idx == y_idx or x_idx == z_idx or y_idx == z_idx:
                continue
            res = min(res, x_val + y_val + z_val)


for x_val, x_idx in x_costs:
    for yz_val, yz_idx in yz_costs:
        if x_idx == yz_idx:
            continue
        res = min(res, x_val + yz_val)

for y_val, y_idx in y_costs:
    for xz_val, xz_idx in xz_costs:
        if y_idx == xz_idx:
            continue
        res = min(res, y_val + xz_val)

for z_val, z_idx in z_costs:
    for xy_val, xy_idx in xy_costs:
        if z_idx == xy_idx:
            continue
        res = min(res, z_val + xy_val)

print(res)

