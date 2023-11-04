class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)
    


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
        
#         l = 0
#         r = len(nums) - 1
            
#         result = 0
#         answer = 0

#         while l <= r:
            
#             if nums[l] < 0:
#                 l += 1
#             elif nums[r] < 0:
#                 r -= 1

#             else:
#                 best = [i for i in range(l, r+1)]
#                 for i in best:
#                     result += nums[i]
#                 answer = max(answer, result)
#                 result = 0
#                 best = []
        
#         print(answer)
#         return answer