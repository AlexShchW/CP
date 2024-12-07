N, D = [int(el) for el in input().split()]

S = input()

cookies = S.count('@')

cookies_left = cookies - D

print(N - cookies_left)