import numpy as np
class Solution:


    def trap(self, height: List[int]) -> int:
        i = 1
        water = 0
        blocks = []
        while i < len(height):
            if height[i] < height[i-1]:
                blocks.append((i-1, height[i-1]))
            lowerblock = (i-1, height[i-1])
            while height[i] > height[i-1] and len(blocks):
                
                water += min(blocks[-1][1] - lowerblock[1], height[i] - lowerblock[1]) * (i - blocks[-1][0] - 1)
                if height[i] >= blocks[-1][1]:
                    lowerblock = blocks.pop()
                else:
                    break
                
            i += 1
        return water



    # def trap(self, height: List[int]) -> int:
    #     i = 1
    #     total_water = 0
    #     while i < len(height):
    #         if height[i] < height[i-1]:
    #             start = i - 1
    #             while height[i] < height[start]:
    #                 # if height[i] > height[i-1]:
    #                 #     total_water += min(height[start], height[i]) - height[i-1]
    #                 if i >= len(height): 
    #                     total_water -= max(0, height[start] - height[i-1]) * ((i-1) - start)
    #                     break
    #                 total_water += height[start] - height[i] 
    #                 i += 1
                
    #         i += 1
    #     return 0







    # def trap(self, height: List[int]) -> int:
    #     height = np.array(height)
    #     level = max(height)
    #     while level >= 1:
    #         height = height/level

    #         for 
    #         print(height/level)

    #         level -= 1
    #     return 0
        


    # def trap(self, height: List[int]) -> int:
    #     total = 0
    #     level = max(height) - 1
    #     while level >= 0:
    #         i = 0
    #         while i < len(height):
    #             if height[i] > level: # black
    #                 i += 1
    #                 subtotal = 0
    #                 while i < len(height):
    #                     if height[i] > level:
    #                         total += subtotal
    #                         break
    #                     subtotal += 1
    #                     i += 1
    #             else:
    #                 i += 1
    #         level -= 1
    #     return total
