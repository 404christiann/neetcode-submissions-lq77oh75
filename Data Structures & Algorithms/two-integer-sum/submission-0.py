class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap which will contain the sums between the elements in nums.
        # the hashmap will look something like this: {sum:[index1,index2]}

        # through each iteration, we will ask if the sum is equal to the target
        # [3,4,5,6] t = 7 
        # a + b = c
        # a+b-c = 0

        # 7 -3 = 4
        # store this 4 into our hashmap, key:4 value: its index (0) 
        # iterate through the nums

        # [4,5,6] t = 10
        hashMap = {}
        for index in range(len(nums)): 
            totalDiff = target - nums[index]
            print(nums[index])
            if nums[index] in hashMap:
                return [hashMap[nums[index]], index]
            hashMap[totalDiff] = index
        print(hashMap)
        return []


        

        
        