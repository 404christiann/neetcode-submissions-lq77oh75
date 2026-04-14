class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a memory bank, starts off empty.
        # iterate through the array
        # during each iteration we want to check if the number exists in the memory bank
        # if it does exist in our memory bank, we have found a duplicate return False
        # if its not in our bank then we can add it to the bank. 

        # Edge Cases: 
        # [1,2,3,3]
        
        memoryBank = []
        for i in nums:
            if i in memoryBank:
                return True
            else:
                memoryBank.append(i)
        return False
