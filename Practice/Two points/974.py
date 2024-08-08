class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i+1] = (prefix_sum[i] + nums[i]) % k
        
        my_dict = {}
        ans = 0
        for i in prefix_sum:
            if i in my_dict:
                ans += my_dict[i]
                my_dict[i] += 1
            else:
                my_dict[i] = 1
            

        return ans
