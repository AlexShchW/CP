N = int(input())

a_arr = [int(el) for el in input().split()]

closest_lesser_to_the_right = [-1] * N

stack = []

for i in range(N - 1, -1, -1):
    while stack and a_arr[stack[-1]] >= a_arr[i]:
        stack.pop()
    if stack:
        closest_lesser_to_the_right[i] = stack[-1]
    stack.append(i)

print(*closest_lesser_to_the_right)
