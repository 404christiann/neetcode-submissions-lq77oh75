class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort both the strings s & t. 
        # Using the sorted method, will gives an array of the sorted characters.
        # Check if the arrays are the same
        # if they are the same then we return True, otherwise False. 

        s = sorted(s)
        t = sorted(t)
        if s == t: 
            return True
        return False