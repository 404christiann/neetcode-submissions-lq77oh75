class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # same concept as the previous bst problem. 
        # start in the middle, potentially search that list to find it and then
        # either pick the list before or after it. 

        left = 0 
        right = len(matrix) - 1

        while left <= right:
            middle = (left + right) // 2
            currList = matrix[middle]
            for element in matrix[middle]:
                if element == target:
                    return True
            # we need to increment which list to look at. 
            if currList and target > currList[0]:
                left = middle + 1
            elif currList and target < currList[0]:
                right = middle - 1
        return False