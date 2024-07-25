class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor_sum = [0]
        for i in arr:
            xor_sum.append(xor_sum[-1] ^ i)
        
        result = []
        for left_i, right_i in queries:
            result.append(xor_sum[right_i+1] ^ xor_sum[left_i])
        
        return result