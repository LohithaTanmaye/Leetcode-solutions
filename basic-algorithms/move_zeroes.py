from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Move all zeroes to the end while keeping other values in order."""
        next_non_zero = 0

        for current in range(len(nums)):
            if nums[current] != 0:
                nums[next_non_zero], nums[current] = nums[current], nums[next_non_zero]
                next_non_zero += 1
