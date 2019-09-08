class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = (k%len(nums))*(-1)
        add = nums[temp:]
        last = nums[:temp]
        nums[:]  = add+last