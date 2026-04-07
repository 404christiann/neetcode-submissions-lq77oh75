class MinStack:

    def __init__(self):
        self.mainStack = []
        # shadow stack list which helped us reduce the time complexity from O(n) to O(1)
        self.minimumStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if len(self.minimumStack) == 0:
            self.minimumStack.append(val)
        else:
            if self.minimumStack[-1] >= val:
                self.minimumStack.append(val)
            else:
                self.minimumStack.append(self.minimumStack[-1])

    def pop(self) -> None:
        self.mainStack.pop()
        self.minimumStack.pop()

    def top(self) -> int:
        if self.mainStack:
            return self.mainStack[-1]
        return None

    def getMin(self) -> int:
        # Using the min( ) function will cause O(n) time, since you have to go through every element in the array.
        # return min(self.mainStack)

        # another approach is getting the minimum from the minimumStack list and grabbing the first or last index
        # however we structure it.
        return self.minimumStack[-1]