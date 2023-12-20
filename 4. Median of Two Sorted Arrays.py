class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArr = []
        i = 0
        j = 0
        newLength = int((len(nums1) + len(nums2)) / 2)
        while i + j < newLength + 1:
            if i < len(nums1) and (j >= len(nums2) or nums1[i] < nums2[j]):
                newArr.append(nums1[i])
                i += 1
            else:
                newArr.append(nums2[j])
                j += 1
        return (newArr[newLength-1] + newArr[newLength])/2 if (((len(nums1) + len(nums2)) / 2) % 1 == 0) else newArr[newLength]
