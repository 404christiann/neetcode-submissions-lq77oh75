class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        # This ensures that even if the search window shrinks to a single element, 
        # you still check it.
        while left <= right: 
            # floor division.
            middle = (left + right) // 2
            # since we know its in ascending (sorted)
            if nums[middle] > target: 
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] == target:
                return middle
        return -1