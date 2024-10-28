coords = []
for _ in range(6):
    coords.append(int(input()))

south_west_corner = coords[0], coords[1]
north_east_corner = coords[2], coords[3]

swimmer_coords = coords[4], coords[5]

def dist_from_P1_to_P2(P1, P2):
    return ((P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2) ** 0.5

def dist_from_C_to_AB(A, B, C):
    AB = (B[0] - A[0], B[1] - A[1])
    BA = (A[0] - B[0], A[1] - B[1])
    AC = (C[0] - A[0], C[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])

    # ABC
    dot_product_BC_BA = BC[0] * BA[0] + BC[1] * BA[1]
    if dot_product_BC_BA <= 0:
        return float('inf')

    # BAC
    dot_product_AB_AC = AB[0] * AC[0] + AB[1] * AC[1]
    if dot_product_AB_AC <= 0:
        return float('inf')

    AB_squared = AB[0] ** 2 + AB[1] ** 2
    projection_length = dot_product_AB_AC / AB_squared
    
    AP_x = projection_length * AB[0]
    AP_y = projection_length * AB[1]
    
    PC_x = AC[0] - AP_x
    PC_y = AC[1] - AP_y
    
    return (PC_x ** 2 + PC_y ** 2) ** 0.5

north_west_corner = south_west_corner[0], north_east_corner[1]
south_east_corner = north_east_corner[0], south_west_corner[1]

res = []
res.append((dist_from_C_to_AB(south_west_corner, north_west_corner, swimmer_coords), "W"))
res.append((dist_from_C_to_AB(north_west_corner, north_east_corner, swimmer_coords), "N"))
res.append((dist_from_C_to_AB(north_east_corner, south_east_corner, swimmer_coords), "E"))
res.append((dist_from_C_to_AB(south_east_corner, south_west_corner, swimmer_coords), "S"))

res.append((dist_from_P1_to_P2(south_west_corner, swimmer_coords), "SW"))
res.append((dist_from_P1_to_P2(north_west_corner, swimmer_coords), "NW"))
res.append((dist_from_P1_to_P2(north_east_corner, swimmer_coords), "NE"))
res.append((dist_from_P1_to_P2(south_east_corner, swimmer_coords), "SE"))

print(min(res)[1])
