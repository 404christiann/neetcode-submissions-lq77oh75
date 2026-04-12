class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # eg. height = [1,7,2,5,4,7,3,6]
        # [2,2,2]
        # You need a pointer in the front of the arr and in the back of the arr. 
        i = 0
        j = len(heights) - 1
        maxWaterAmount = 0 
        while i < j:
            # we need to find the largest area covered, the minimum bar will be its length 
            # the width will be the distance from index A to index B.  
            length = min(heights[i], heights[j])
            width = j - i
            currentWaterAmount = length * width
            maxWaterAmount = max(currentWaterAmount, maxWaterAmount)
            # to find the largest area, we remove the shorter bar.
            if heights[i] < heights[j]:
                i+=1
            elif heights[j] <= heights[i]:
                j-=1

        print(maxWaterAmount)
        return maxWaterAmount
