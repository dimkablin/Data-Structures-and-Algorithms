class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        my_dict = {}
        i_sum = 0
        ans = 0
        for i in range(k):
            i_sum += nums[i]
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
        if len(my_dict) >= m:
            ans = i_sum
        
        for i in range(k, len(nums)):
            # add nums[i]
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
            i_sum += nums[i]
            
            # delete nums[i-k]
            my_dict[nums[i-k]] -= 1
            if my_dict[nums[i-k]] == 0:
                del my_dict[nums[i-k]]
            i_sum -= nums[i-k]

            if len(my_dict) >= m:
                ans = max(ans, i_sum)
            
        return ans
