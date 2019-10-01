class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max((nums[0],nums[1]))
        
        
        robbed = [0 for _ in range(len(nums))]
        robbed[0] = nums[0]
        robbed[1] = max(nums[0], nums[1])
        robbed[2] = max((nums[0]+nums[2]), nums[1])
        
        
        for i in range(3, len(nums)):
            robbed[i] = max((robbed[i-2]+nums[i]), robbed[i-1])
        return(max(robbed))