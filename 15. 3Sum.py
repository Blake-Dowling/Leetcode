class Solution:
    def twoSum(self, nums, val):
        left = 0
        right = len(nums)-1
        triplets = []
        while left < right:
            sum = nums[left] + nums[right]
            if sum == (-val):
                triplets.append([val, nums[left], nums[right]])
            if sum > -val:
                while right-1 >= 0 and nums[right-1] == nums[right]:
                    right -= 1
                right -= 1
            else:
                while left+1 < len(nums) and nums[left+1] == nums[left]:
                    left += 1
                left += 1
        return triplets
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        triplets = []
        while i < len(nums):
            newTriplets = self.twoSum(nums[i+1:], nums[i])
            if len(newTriplets):
                for t in newTriplets:
                    triplets.append(t)
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return triplets