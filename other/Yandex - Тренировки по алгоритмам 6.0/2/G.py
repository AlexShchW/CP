n, c = [int(el) for el in input().split()]

s = input()

res = 0

have_a = 0
have_b = 0
cur_bad = 0
left, right = 0, 0
while left < n and right < n:
    while right < n:
        if s[right] == "a":
            have_a += 1
        if s[right] == "b":
            have_b += 1
            cur_bad += have_a
        right += 1
        if cur_bad <= c:
            res = max(res, right - left)
        else:
            break
    if right == n:
        break
    while left < n:
        if s[left] == "a":
            have_a -= 1
            cur_bad -= have_b
        if s[left] == "b":
            have_b -= 1
        left += 1
        if cur_bad <= c:
            res = max(res, right - left)
            break

print(res)

