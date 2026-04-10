class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # recall the equation: A + B + C = 0
        # A + B + C == -A = B + C
        nums.sort()
        # eg. [-4, -1, -1 , 0, 1, 2]
        allThreeSums = []
        # processedIntegers = ()
        for i in range(len(nums)):
            # conditional needed for duplicate case. 
            # this helps skipping any duplicate triplets. 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1 
            zeroSum = -1 * nums[i]
            while j < k:
                totalSum = nums[i] + nums[j] + nums[k] 
                if totalSum == 0:
                    allThreeSums.append([nums[i],nums[j],nums[k]])
                    # after adding this to our final output list, we still need to move j & k. 
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif totalSum > 0:
                    k -= 1 
                elif totalSum < 0:
                    # if the total sum is too small lets increase j.
                    j += 1
        return allThreeSums
        