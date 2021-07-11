#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        middle = int((m + n) / 2)
        isEven = True if (m + n) % 2 == 0 else False
        i = j = 0
        cnt = 0
        result = []
        while (True):
            if (cnt > middle):
                break
            if (m - i == 0):
                result.append(nums2[j])
                j += 1
            elif (n - j == 0):
                result.append(nums1[i])
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    result.append(nums1[i])
                    i += 1
                else:
                    result.append(nums2[j])
                    j += 1
            cnt += 1
        
        if isEven:
            return (result[middle -1] + result[middle]) / 2
        else:
            return result[middle]

def main():
    list1 = [1, 3]
    list2 = [2]
    print(Solution().findMedianSortedArrays(list1, list2))

if __name__ == "__main__":
    main()

# @lc code=end

