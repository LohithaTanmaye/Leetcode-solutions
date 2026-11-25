from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Return the target index in a sorted list, or -1 if it is absent."""
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1
