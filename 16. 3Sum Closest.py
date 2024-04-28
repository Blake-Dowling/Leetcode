class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        x = 0
        closestSum = sys.maxsize
        while x < len(nums) - 2:
            y = x + 1
            z = len(nums) - 1
            while y < z:
                sum = nums[x] + nums[y] + nums[z]
                if abs(target - sum) < abs(target - closestSum):
                    closestSum = sum
                elif abs(target - sum) == abs(target - closestSum) and sum < closestSum:
                    closest = sum
                if sum > target:
                    while z > y and nums[z-1] == nums[z]:
                        z -= 1
                    z -= 1
                else:
                    while y < z and nums[y+1] == nums[y]:
                        y += 1
                    y += 1
            while x < len(nums) - 2 and nums[x+1] == nums[x]:
                x+= 1
            x += 1
        return closestSum