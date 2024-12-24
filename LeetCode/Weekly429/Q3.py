class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        s = [int(el) for el in list(s)]
        N = len(s)
        segments = []
        cur_el = s[0]
        cur_l = 1
        for el in s[1:]:
            if el == cur_el:
                cur_l += 1
            else:
                segments.append(cur_l)
                cur_el = el
                cur_l = 1
        segments.append(cur_l)
        
        def longest_is_l_or_lower(l):
            
            if l == 1:
                wasted = 0
                prev = s[0]
                for el in s[1:]:
                    if prev != el:
                        prev = el
                        continue
                    wasted += 1
                    prev = el ^ 1
                if wasted <= numOps:
                    return True
                if wasted > numOps and numOps == 0:
                    return False
                
                # change first
                wasted = 1
                prev = s[0] ^ 1
                for el in s[1:]:
                    if prev != el:
                        prev = el
                        continue
                    wasted += 1
                    prev = el ^ 1
                return wasted <= numOps

            ops_wasted = 0
            for i in range(len(segments)):
                el = segments[i]
                sub_segments = el // (l + 1)
                ops_wasted += sub_segments
            return ops_wasted <= numOps
                

        l, r = 1, N
        res = None
        while l <= r:
            p = (l + r) // 2
            if longest_is_l_or_lower(p):
                res = p
                r = p - 1
            else:
                l = p + 1
        return res