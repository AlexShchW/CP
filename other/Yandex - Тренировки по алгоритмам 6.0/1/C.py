import collections

n = int(input())
field = []
for _ in range(n):
    row = input()
    field.append(row)


def find_connected_components_of_symb_in_area(symbol, *borders):
    top_border, left_border, bottom_border, right_border = borders
    visited = [[False] * n for _ in range(n)]

    def check_component_to_be_rectangular(component):
        top_left = component[0]
        bottom_right = component[-1]
        for i in range(top_left[0], bottom_right[0] + 1):
            for j in range(top_left[1], bottom_right[1] + 1):
                if field[i][j] != symbol:
                    return False
        for x, y in component:
            if x < top_left[0] or x > bottom_right[0]:
                return False
            if y < top_left[1] or y > bottom_right[1]:
                return False
        return True
    
    def find_component(i, j):
        q = collections.deque([(i, j)])
        component = []
        while q:
            x, y = q.popleft()
            component.append((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nx, ny = x + dx, y + dy
                if top_border <= nx <= bottom_border and left_border <= ny <= right_border and not visited[nx][ny] and field[nx][ny] == symbol:
                    visited[nx][ny] = True
                    q.append((nx, ny))
        component.sort()
        status = check_component_to_be_rectangular(component)
        top_left = component[0]
        bottom_right = component[-1]
        bottom_left = bottom_right[0], top_left[1]
        top_right = top_left[0], bottom_right[1]
        return status, top_left, bottom_right, bottom_left, top_right, component.copy()
    
    components = []
    for i in range(top_border, bottom_border + 1):
        for j in range(left_border, right_border + 1):
            if visited[i][j]:
                continue
            if field[i][j] != symbol:
                visited[i][j] = True
                continue
            visited[i][j] = True
            status, top_left, bottom_right, bottom_left, top_right, component = find_component(i, j)
            components.append((status, top_left, bottom_right, bottom_left, top_right, component))
    return components


def check_for_O(*borders):
    components = find_connected_components_of_symb_in_area(".", *borders)
    top_border, left_border, bottom_border, right_border = borders
    if len(components) != 1:
        return False
    if not components[0][0]:
        return False
    top_left, bottom_right, bottom_left, top_right = components[0][1], components[0][2], components[0][3], components[0][4]
    if top_left[0] == top_border or top_left[1] == left_border:
        return False
    if bottom_right[0] == bottom_border or bottom_right[1] == right_border:
        return False
    if bottom_left[0] == bottom_border or bottom_left[1] == left_border:
        return False
    if top_right[0] == top_border or top_right[1] == right_border:
        return False
    return True
    

def check_for_C(*borders):
    components = find_connected_components_of_symb_in_area(".", *borders)
    top_border, left_border, bottom_border, right_border = borders
    if len(components) != 1:
        return False
    if not components[0][0]:
        return False
    top_left, bottom_right, bottom_left, top_right = components[0][1], components[0][2], components[0][3], components[0][4]
    if top_left[0] == top_border or top_left[1] == left_border:
        return False
    if bottom_right[0] == bottom_border or bottom_right[1] != right_border:
        return False
    if bottom_left[0] == bottom_border or bottom_left[1] == left_border:
        return False
    if top_right[0] == top_border or top_right[1] != right_border:
        return False
    return True


def check_for_L(*borders):
    components = find_connected_components_of_symb_in_area(".", *borders)
    top_border, left_border, bottom_border, right_border = borders
    if len(components) != 1:
        return False
    if not components[0][0]:
        return False
    top_left, bottom_right, bottom_left, top_right = components[0][1], components[0][2], components[0][3], components[0][4]
    if top_left[0] != top_border or top_left[1] == left_border:
        return False
    if bottom_right[0] == bottom_border or bottom_right[1] != right_border:
        return False
    if bottom_left[0] == bottom_border or bottom_left[1] == left_border:
        return False
    if top_right[0] != top_border or top_right[1] != right_border:
        return False
    return True
    

def check_for_H(*borders):
    components = find_connected_components_of_symb_in_area(".", *borders)
    top_border, left_border, bottom_border, right_border = borders
    if len(components) != 2:
        return False
    if not components[0][0] or not components[1][0]:
        return False
    top_left_1, bottom_right_1, bottom_left_1, top_right_1 = components[0][1], components[0][2], components[0][3], components[0][4]
    top_left_2, bottom_right_2, bottom_left_2, top_right_2 = components[1][1], components[1][2], components[1][3], components[1][4]
    if top_left_1[1] != top_left_2[1]:
        return False
    if top_right_1[1] != top_right_2[1]:
        return False
    if top_left_1[1] == left_border or top_right_1[1] == right_border:
        return False
    if top_left_1[0] != top_border or bottom_left_2[0] != bottom_border:
        return False
    return True
    

def check_for_P(*borders):
    components = find_connected_components_of_symb_in_area(".", *borders)
    top_border, left_border, bottom_border, right_border = borders
    if len(components) != 2:
        return False
    if not components[0][0] or not components[1][0]:
        return False
    top_left_1, bottom_right_1, bottom_left_1, top_right_1 = components[0][1], components[0][2], components[0][3], components[0][4]
    top_left_2, bottom_right_2, bottom_left_2, top_right_2 = components[1][1], components[1][2], components[1][3], components[1][4]

    if top_left_1[0] == top_border or top_left_1[1] == left_border:
        return False
    if top_right_1[1] == right_border:
        return False
    if bottom_left_1[0] == bottom_border:
        return False
    
    if top_left_1[1] != top_left_2[1]:
        return False
    if top_right_2[1] != right_border:
        return False
    if bottom_left_2[0] != bottom_border:
        return False
    return True


def solve():
    turned_on_components = find_connected_components_of_symb_in_area("#", 0, 0, n - 1, n - 1)
    if len(turned_on_components) != 1:
        return "X"
    if turned_on_components[0][0]:
        return "I"
    
    top_border, left_border, bottom_border, right_border = n, n, 0, 0

    for i, j in turned_on_components[0][5]:
        top_border = min(top_border, i)
        left_border = min(left_border, j)
        bottom_border = max(bottom_border, i)
        right_border = max(right_border, j)
    
    borders = [top_border, left_border, bottom_border, right_border]
    
    if check_for_O(*borders):
        return "O"
    if check_for_C(*borders):
        return "C"
    if check_for_L(*borders):
        return "L"
    if check_for_H(*borders):
        return "H"
    if check_for_P(*borders):
        return "P"
    return "X"

    
print(solve())


