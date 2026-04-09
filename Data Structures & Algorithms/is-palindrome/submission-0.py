from collections import Counter
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all the non-alphanumeric in the string.
        # racecar
        s = s.lower()
        alphanumericString = ''
        reversed_string = ''
        for characterValue in s:
            if characterValue.isalnum():
                alphanumericString += characterValue
        for valid_value in reversed(alphanumericString):
            reversed_string += valid_value

        return alphanumericString == reversed_string

            


            
        