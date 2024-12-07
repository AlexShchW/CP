class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(t)
        substrings_length = n // k
        s_counter = collections.Counter()
        t_counter = collections.Counter()
        for i in range(len(s)):
            cur_s_substring = s[i : i + substrings_length]
            s_counter[cur_s_substring] += 1
            cur_t_substring = t[i : i + substrings_length]
            t_counter[cur_t_substring] += 1
        for key in s_counter:
            if s_counter[key] != t_counter[key]:
                print(key, s_counter[key], t_counter[key])
                return False
        return True
