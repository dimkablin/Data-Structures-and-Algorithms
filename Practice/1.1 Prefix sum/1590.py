class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p

        if remainder == 0:
            return 0

        prefix_sum = 0
        min_length = n = len(nums)
        prefix_map = {0: -1}  # Префиксная сумма до начала массива

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            target = (prefix_sum - remainder) % p

            if target in prefix_map:
                min_length = min(min_length, i - prefix_map[target])
            
            prefix_map[prefix_sum] = i

        return min_length if min_length < n else -1
