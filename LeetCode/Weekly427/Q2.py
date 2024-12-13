class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        storage_x = collections.defaultdict(list)
        storage_y = collections.defaultdict(list)
        points_dict = {}

        for i, (x, y) in enumerate(points):
            storage_x[x].append(i)
            storage_y[y].append(i)
            points_dict[(x, y)] = i

        res = -1
        N = len(points)

        for i_a in range(N):
            A = points[i_a]
            for i_b in range(N):
                if i_b == i_a:
                    continue
                B = points[i_b]
                
                if A[1] != B[1]:
                    continue
                
                for i_c in range(N):
                    if i_c == i_a or i_c == i_b:
                        continue
                    C = points[i_c]
                    
                    if A[0] != C[0]:
                        continue
                    
                    D = (B[0], C[1])
                    if D not in points_dict:
                        continue
                    i_d = points_dict[D]
                    
                    if i_d == i_c or i_d == i_b or i_d == i_a:
                        continue
                    
                    there_is_inside = False
                    for i_o, (x, y) in enumerate(points):
                        if i_o == i_a or i_o == i_b or i_o == i_c or i_o == i_d:
                            continue
                        if B[0] <= x <= A[0] or A[0] <= x <= B[0]:
                            if C[1] <= y <= A[1] or A[1] <= y <= C[1]:
                                there_is_inside = True
                                break
                    if there_is_inside:
                        continue
                    
                    cur_area = abs(A[0] - B[0]) * abs(C[1] - A[1])
                    res = max(res, cur_area)
        
        return res




