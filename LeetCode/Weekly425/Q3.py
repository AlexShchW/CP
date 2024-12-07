class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:


        storage = [[[None] * N for _ in range(op1 + 1)] for __ in range(op2 + 1)]


        def f(cur_idx, op1_left, op2_left):
            if cur_idx == N:
                return 0
            if storage[op2_left][op1_left][cur_idx] is not None:
                return storage[op2_left][op1_left][cur_idx]
            
            if not op1_left and not op2_left:
                storage[op2_left][op1_left][cur_idx] = nums[cur_idx] + f(cur_idx + 1, op1_left, op2_left)
                return storage[op2_left][op1_left][cur_idx]
            
            if op1_left and not op2_left:
                using_op1 = math.ceil(nums[cur_idx] / 2) + f(cur_idx + 1, op1_left - 1, op2_left)
                not_using_op1 = nums[cur_idx] + f(cur_idx + 1, op1_left, op2_left)
                storage[op2_left][op1_left][cur_idx] = min(using_op1, not_using_op1)
                return storage[op2_left][op1_left][cur_idx]
            if not op1_left and op2_left:
                using_op2 = float('inf')
                if nums[cur_idx] >= k:
                    using_op2 = nums[cur_idx] - k + f(cur_idx + 1, op1_left, op2_left - 1)
                not_using_op2 = nums[cur_idx] + f(cur_idx + 1, op1_left, op2_left)
                storage[op2_left][op1_left][cur_idx] = min(using_op2, not_using_op2)
                return storage[op2_left][op1_left][cur_idx]
            
            using_op1 = math.ceil(nums[cur_idx] / 2) + f(cur_idx + 1, op1_left - 1, op2_left)
            using_op2 = float('inf')
            if nums[cur_idx] >= k:
                using_op2 = nums[cur_idx] - k + f(cur_idx + 1, op1_left, op2_left - 1)
            not_using_any_op = nums[cur_idx] + f(cur_idx + 1, op1_left, op2_left)
            using_op1_then_op2 = float('inf')
            using_op2_then_op1 = float('inf')
            if nums[cur_idx] >= k:
                new_elem = math.ceil(nums[cur_idx] / 2)
                if new_elem >= k:
                    using_op1_then_op2 = new_elem - k + f(cur_idx + 1, op1_left - 1, op2_left - 1)
                using_op2_then_op1 = math.ceil((nums[cur_idx] - k) / 2) + f(cur_idx + 1, op1_left - 1, op2_left - 1)
            storage[op2_left][op1_left][cur_idx] = min(using_op1, using_op2, not_using_any_op, using_op1_then_op2, using_op2_then_op1)
            return storage[op2_left][op1_left][cur_idx]
        
        return f(0, op1, op2)
