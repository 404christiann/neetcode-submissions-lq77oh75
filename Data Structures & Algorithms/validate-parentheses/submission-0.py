class Solution:
    def isValid(self, s: str) -> bool:
        # you can have nested brackets.
        bracket_stack = []
        for bracket in s:
            if bracket in "([{":
                # Opening move
                bracket_stack.append(bracket)
            elif not bracket_stack:
                return False
            elif bracket == "]":
                if not bracket_stack or bracket_stack[-1] != "[":
                    return False
                bracket_stack.pop() # Match found! Remove the '[' and keep going.
            elif bracket == "}":
                if not bracket_stack or bracket_stack[-1] != "{":
                    return False
                bracket_stack.pop()
            elif bracket == ")":
                if not bracket_stack or bracket_stack[-1] != "(":
                    return False
                bracket_stack.pop()
        if len(bracket_stack) == 0:
            return True
        return False
