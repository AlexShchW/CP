n = int(input())

interestness_arr = [int(el) for el in input().split()]

usefulness_arr = [int(el) for el in input().split()]

mood_arr = [int(el) for el in input().split()]

combined_with_interestness_as_main = sorted([(interestness_arr[i], usefulness_arr[i], -i) for i in range(n)])
combined_with_usefulness_as_main = sorted([(usefulness_arr[i], interestness_arr[i], -i) for i in range(n)])

idxs_took = set()
res = []

for i in range(n):
    if not mood_arr[i]:
        while -combined_with_interestness_as_main[-1][2] in idxs_took:
            combined_with_interestness_as_main.pop()
        idx = -combined_with_interestness_as_main.pop()[2]
        idxs_took.add(idx)
        res.append(idx + 1)
    else:
        while -combined_with_usefulness_as_main[-1][2] in idxs_took:
            combined_with_usefulness_as_main.pop()
        idx = -combined_with_usefulness_as_main.pop()[2]
        idxs_took.add(idx)
        res.append(idx + 1)

print(*res)
