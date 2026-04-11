class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # key formula to this problem: A + B + C = 0
        # we can refactor this equation to look like this. 
        # B + C = -A
        nums.sort()
        memory_bank = {}
        finalOutput = []
        # nums = [-1,0,1,2,-1,-4]
        # we are going to use i as an "anchor"
        # [-4,-1,-1,0,1,2]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: 
                    continue
            j = i+1 
            k = len(nums) - 1
            while j < k: 
                totalSum = nums[i] + nums[k] + nums[j]
                if totalSum == 0: 
                    finalOutput.append([nums[i], nums[k], nums[j]])
                    # after finding a sum thats equal to zero, we still 
                    # need to 
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j+=1
                    k-=1
                if totalSum > 0: 
                    # the sum is too big.
                    # decrease k
                    k -= 1 
                elif totalSum < 0:
                    # increase i 
                    j+=1
        return finalOutput






