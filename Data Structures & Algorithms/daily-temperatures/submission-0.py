class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # the last element in the array will never have a future day.
        # think stack, stacks, stacks, and stacks.
        result = [0] * len(temperatures)
        temperature_index_stack = []
        for curr_idx in range(len(temperatures)):
            # look backwards, for the [50,40,60] example we finally get to 60(a big number) then we start
            # taking the difference (distance) from each index from that element. (temperatures[curr_idx] > temperatures[temp_stack[-1]])
            while temperature_index_stack and temperatures[curr_idx] > temperatures[temperature_index_stack[-1]]:
                prev_idx = temperature_index_stack.pop()
                # distance between temperatures
                result[prev_idx] = curr_idx - prev_idx
            # Push the current day's index onto the stack to wait for its own warmer day
            temperature_index_stack.append(curr_idx)
        return result