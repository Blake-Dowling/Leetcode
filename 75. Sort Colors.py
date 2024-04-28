class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        y = 0
        z = len(nums)-1
        while y <= z:
            if nums[y] == 0:
                nums[y] = nums[x]
                nums[x] = 0
                x += 1
                y += 1
            elif nums[y] == 2:
                nums[y] = nums[z]
                nums[z] = 2
                z -= 1
            elif nums[y] == 1:
                y += 1
