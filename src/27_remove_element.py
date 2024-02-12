# Problem ref: https://leetcode.com/problems/remove-element/description/

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

from typing import List

class Solution:
    def removeElement2(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        n = len(nums)

        while i <n:
            if nums[i] != val:
                nums[j]  = nums[i]
                j += 1
            i += 1

        return j

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n
    

nums = [[3,2,2,3], [0,1,2,2,3,0,4,2]]
val = [3, 2]
result = [[2,2],[0,0,1,3,4]]

test_cases = len(val)

sol = Solution()

for i in range(test_cases):
    k = sol.removeElement(nums[i], val[i])
    assert k == len(result[i]), "Expected array length: {x}, actual array lenth: {k}".format(x = len(result[i]), y = k)
    check = nums[i][:k]
    check.sort()
    assert check == result[i], "Expected array: {x}, Actual array: {y}".format(x = result[i], y = check)




# Complexity: O(n)/O(1)

# The trick for solving this problem is to use two pointers. One for iterating all numbers and the other for iterating acceptable numbers. 
# If we can assume that the number of remove value is less than the total array size then removeElement will perform better than removeElement2 (due to the less number of assignment operations). Since, the result do not care assignment orders we can replace the last value to the removed space and make our actual array smaller by shrinking the end pointer. 

# For interviews, there is a high chance that the interviewer would ask a follow-up to implement removeElement if your intial implementation is removeElement2 and vice-versa. Therefore, understanding both of the approaches clearly is recommended.