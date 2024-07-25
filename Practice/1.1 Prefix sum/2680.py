from itertools import accumulate


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        bitwiseOr = lambda x, y: x | y
        
        forward = list(accumulate(nums, bitwiseOr))
        backward = list(accumulate(nums[ : : -1], bitwiseOr))[ : : -1]
        
        forward = [0] + forward[ : -1]
        backward = backward[1 : ] + [0]
        
        res = 0
        
        for i in range(len(nums)):
            total = forward[i] | backward[i]
            t = nums[i] * pow(2, k)
            
            res = max(res, total | t)
        
        return res


class NaiveSolution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        bits = [0]*32

        for num in nums:
            for i in range(32):
                if num & (1 << i) > 0:
                    bits[i] += 1

        best = 0
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bits[i] -= 1
             
            current = 0
            for i in range(32):
                if bits[i] > 0:
                    current += (1 << i)
            current |= num * (1 << k)
            best = max(current, best)

            for i in range(32):
                if num & (1 << i):
                    bits[i] += 1
        
        return best