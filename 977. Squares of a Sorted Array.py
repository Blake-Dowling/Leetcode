class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        newArr = [0 for i in range(len(nums))]
        while left <= right:
            leftSquare = nums[left]**2
            rightSquare = nums[right]**2
            if leftSquare > rightSquare:
                newArr[right-left] = leftSquare
                left += 1
            else:
                newArr[right-left] = rightSquare
                right -= 1
        return newArr