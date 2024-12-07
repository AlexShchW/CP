import random
import itertools
import sys

n, W = map(int, sys.stdin.readline().split())
h_arr = list(map(int, sys.stdin.readline().split()))
w_arr = list(map(int, sys.stdin.readline().split()))

def get_res():
    if max(w_arr) >= W or n == 1:
        return 0
    combined_arr = sorted(list(zip(h_arr, w_arr)))

    diffs = [0] * (n - 1)
    for i in range(1, n):
        diffs[i - 1] = combined_arr[i][0] - combined_arr[i - 1][0]
    
    idx_of_closest_larger_element_to_the_right = [None] * len(diffs)
    stack = []
    for i in range(len(diffs) - 1, -1, -1):
        while stack and diffs[stack[-1]] <= diffs[i]:
            stack.pop()
        idx_of_closest_larger_element_to_the_right[i] = stack[-1] if stack else None
        stack.append(i)
    idx_of_closest_larger_element_to_the_left = [None] * len(diffs)
    stack = []
    for i in range(len(diffs)):
        while stack and diffs[stack[-1]] <= diffs[i]:
            stack.pop()
        idx_of_closest_larger_element_to_the_left[i] = stack[-1] if stack else None
        stack.append(i) 

    prefix_sums = [0] * n
    cur_sum = 0
    for i in range(n):
        cur_sum += combined_arr[i][1]
        prefix_sums[i] = cur_sum
    # print(combined_arr)
    # print(prefix_sums)
    left, right = 0, 1
    res = float('inf')
    while right < n:
        max_diff_allowed = combined_arr[right][0] - combined_arr[left][0]
        this_diff_idx = left 
        first_larger_to_the_right_idx = idx_of_closest_larger_element_to_the_right[this_diff_idx]
        first_larger_to_the_left_idx = idx_of_closest_larger_element_to_the_left[this_diff_idx]
        last_el_idx = n - 1
        first_el_idx = 0
        if first_larger_to_the_right_idx is not None:
            last_el_idx = first_larger_to_the_right_idx
        if first_larger_to_the_left_idx is not None:
            first_el_idx = first_larger_to_the_left_idx + 1
        
        # print(left, right, first_el_idx, last_el_idx)
        width = prefix_sums[last_el_idx] - prefix_sums[first_el_idx - 1] if first_el_idx != 0 else prefix_sums[last_el_idx]
        if width >= W:
            res = min(res, max_diff_allowed)
        left += 1
        right += 1
    return res

print(get_res())

def my_func(n, W, h_arr, w_arr):

    def get_res():
        if max(w_arr) >= W or n == 1:
            return 0
        combined_arr = sorted(list(zip(h_arr, w_arr)))

        diffs = [0] * (n - 1)
        for i in range(1, n):
            diffs[i - 1] = combined_arr[i][0] - combined_arr[i - 1][0]

        idx_of_closest_larger_element_to_the_right = [None] * len(diffs)
        stack = []
        for i in range(len(diffs) - 1, -1, -1):
            while stack and diffs[stack[-1]] <= diffs[i]:
                stack.pop()
            idx_of_closest_larger_element_to_the_right[i] = stack[-1] if stack else None
            stack.append(i)
        idx_of_closest_larger_element_to_the_left = [None] * len(diffs)
        stack = []
        for i in range(len(diffs)):
            while stack and diffs[stack[-1]] <= diffs[i]:
                stack.pop()
            idx_of_closest_larger_element_to_the_left[i] = stack[-1] if stack else None
            stack.append(i) 

        prefix_sums = [0] * n
        cur_sum = 0
        for i in range(n):
            cur_sum += combined_arr[i][1]
            prefix_sums[i] = cur_sum
        # print(combined_arr)
        # print(prefix_sums)
        left, right = 0, 1
        res = float('inf')
        while right < n:
            max_diff_allowed = combined_arr[right][0] - combined_arr[left][0]
            this_diff_idx = left 
            first_larger_to_the_right_idx = idx_of_closest_larger_element_to_the_right[this_diff_idx]
            first_larger_to_the_left_idx = idx_of_closest_larger_element_to_the_left[this_diff_idx]
            last_el_idx = n - 1
            first_el_idx = 0
            if first_larger_to_the_right_idx is not None:
                last_el_idx = first_larger_to_the_right_idx
            if first_larger_to_the_left_idx is not None:
                first_el_idx = first_larger_to_the_left_idx + 1
            
            # print(left, right, first_el_idx, last_el_idx)
            width = prefix_sums[last_el_idx] - prefix_sums[first_el_idx - 1] if first_el_idx != 0 else prefix_sums[last_el_idx]
            if width >= W:
                res = min(res, max_diff_allowed)
            left += 1
            right += 1
        return res

    return(get_res())

def brute_force(n, W, h_arr, w_arr):
    res = float('inf')
    def generate_permutations(max_number):
        for r in range(1, max_number + 1):
            for perm in itertools.permutations(range(max_number), r):
                yield tuple(perm)
    
    for perm in generate_permutations(n):
        cur_w = 0
        cur_h = 0
        for idx in perm:
            cur_w += w_arr[idx]

        if len(perm) > 1:
            left, right = 0, 1
            while right < len(perm):
                cur_h = max(cur_h, abs(h_arr[perm[right]] - h_arr[perm[left]]))
                left += 1
                right += 1
        if cur_w >= W:
            res = min(res, cur_h)
        last_perm = perm
        
    return res, last_perm

        

def check():
    tests_conducted = 0
    wrongs_tests = 0
    for _ in range(100):
        n = random.randint(1, 5)
        h_arr = [random.randint(1, 100) for _ in range(n)]
        w_arr = [random.randint(1, 100) for _ in range(n)]
        W = random.randint(1, 100)
        if sum(w_arr) < W:
            continue
        tests_conducted += 1
        my_res = my_func(n, W, h_arr, w_arr)
        brute_force_res, brute_force_perm = brute_force(n, W, h_arr, w_arr)
        if my_res != brute_force_res:
            wrongs_tests += 1
            print(n, W, h_arr, w_arr)
            print(my_res, brute_force_res)
            print(brute_force_perm)
            break
    print(f'Tests conducted: {tests_conducted}')
    print(f'Wrong tests: {wrongs_tests}')

# check()

