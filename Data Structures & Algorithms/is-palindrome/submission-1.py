from collections import Counter
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all the non-alphanumeric in the string.
        # racecar
        #preprocessing step.
        # using two pointers: start at the 0th index and the last index 
        # at the same time. 
        # 'wasitacaroracatisaw?'
        # "abba"
        # "abcba"
        start_idx = 0
        end_idx = len(s) - 1
        while start_idx < end_idx:
            # before you even start comparing chars, ignore all non alphanumerics 
            # one thing to note, .isalnum() will take care of the white space, so dont worry about it. 
            while start_idx < end_idx and not s[start_idx].isalnum():
                start_idx += 1
            while start_idx < end_idx and not s[end_idx].isalnum():
                end_idx -= 1
            # Now we start comparing and lower case letters for efficiency. 
            if s[start_idx].lower() == s[end_idx].lower():
                start_idx += 1
                end_idx -= 1
            else: 
                return False
        return True
            


            
        