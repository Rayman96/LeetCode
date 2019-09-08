class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        else:
            for index, number in enumerate(nums):
                if number == target or number > target:
                    return index
