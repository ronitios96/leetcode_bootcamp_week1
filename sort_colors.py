class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Two pointers: one for 0s (left), one for 2s (right)
        left = 0
        right = len(nums) - 1

        # Current index to scan through the array
        current = 0

        while current <= right:
            if nums[current] == 0:
                # If current element is red (0), swap with left pointer
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                # If current element is blue (2), swap with right pointer
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
                # Note: Don't increment current here as the swapped element needs to be checked
            else:
                # If current element is white (1), just move forward
                current += 1
                
#https://leetcode.com/problems/sort-colors/
