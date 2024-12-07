class Solution:
    def minOperations(self, n: int, m: int) -> int:
        
        def sieve_of_eratosthenes(N):
            primes = [True for _ in range(N + 1)]
            p = 2
            while (p * p <= N):
                if primes[p]:
                    for i in range(p * p, N + 1, p):
                        primes[i] = False
                p += 1
            prime_numbers = [p for p in range(2, N) if primes[p]]
            return prime_numbers
        
        primes = set(sieve_of_eratosthenes(max(n, m) + 10))
        if m in primes or n in primes:
            return -1
        
        h = [(n, n)]
        visited = set()
        visited.add(n)
        while h:
            cost, cur_num = heapq.heappop(h)
            if cur_num == m:
                return cost
            cur_num_str = list([int(el) for el in str(cur_num)])
            poss_next = []
            for i in range(len(cur_num_str)):
                if cur_num_str[i] != 0:
                    poss_next.append(cur_num_str[:i] + [cur_num_str[i] - 1] + cur_num_str[i + 1:])
                if cur_num_str[i] != 9:
                    poss_next.append(cur_num_str[:i] + [cur_num_str[i] + 1] + cur_num_str[i + 1:])
            for next_num in poss_next:
                next_num = int(''.join(map(str, next_num)))
                if next_num not in visited and next_num not in primes:
                    visited.add(next_num)
                    heapq.heappush(h, (cost + next_num, next_num))
        return -1


       