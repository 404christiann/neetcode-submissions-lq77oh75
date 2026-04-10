class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_idx = 0
        end_idx = len(numbers) - 1 
        while start_idx < end_idx: 
            indicies_sum = numbers[start_idx] + numbers[end_idx]
            # think of the thermostat example, if the sum is too big, we need to reduce
            # that big number. 
            if indicies_sum > target: 
                end_idx -= 1
            # vice versa, if the number is too small, we need to increase our small number from the 
            # start_idx since its sorted we know the small number is on the right side. 
            elif indicies_sum < target:
                start_idx += 1
            else: 
                # the problem says 1-indexed, so if an answer is at [0,1] then 
                # the output should be [1,2]
                print([start_idx + 1, end_idx + 1])
                return [start_idx + 1, end_idx + 1]
        return []