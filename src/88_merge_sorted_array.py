# Problem ref: https://leetcode.com/problems/merge-sorted-array/description/

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

from typing import List

class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i , j = m-1, n-1
        k = m + n - 1

        while k >= 0 and j >= 0 and i >= 0:
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
        
        # When loop terminates but still some values from second array is not copied
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i , j = m-1, n-1
        k = m + n - 1

        while k >= 0 and j >= 0:
            if i >= 0:
                if nums2[j] >= nums1[i]:
                    nums1[k] = nums2[j]
                    j -= 1
                    k -= 1
                else:
                    nums1[k] = nums1[i]
                    i -= 1
                    k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1                

nums1 = [[1,2,3,0,0,0], [1],[0],[2,0]]
nums2 = [[2,5,6], [],[1],[1]]
m = [3,1,0,1]
n = [3,0,1,1]
result = [[1,2,2,3,5,6],[1],[1],[1,2]]

test_cases = len(m)

sol = Solution()

for i in range(test_cases):
    sol.merge(nums1[i], m[i], nums2[i], n[i])
    assert nums1[i] == result[i], "Expected: {x}, Actual: {y}".format(x = result[i], y = nums1[i])




# Complexity: O(n)/O(1)

# The trick for solving this problem is preety simple. First, you need to start from the end. Cause all 0s are placed in the end of num1. Therefore starting from end to start is efficient. 
# You do not need to worry about data loss in num1 due to the merge then.
# The other trivk to notice is the j>=0 when i<0 part. In this part we should stop checking nums1[i]. Cause negative index in python will return trailing values of nums1 that we do not want.
