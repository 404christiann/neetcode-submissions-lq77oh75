class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        current_stack = []
        for i in tokens:
            if i in "+-*/":
                # Add the two to the left of the operator.
                # pop twice.
                result = 0
                num2 = current_stack.pop()
                num1 = current_stack.pop()
                if i == "+":
                    result = num1 + num2
                elif i == "-":
                    result = num1 - num2
                elif i == "*":
                    result = num1 * num2
                elif i == "/":
                    result = int (num1 / num2)
                current_stack.append(result)
            else:
                current_stack.append(int(i))

        return current_stack.pop()