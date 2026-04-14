class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            # sort both the strings s & t. 
            # Using the sorted method, will gives an array of the sorted characters.
            # Check if the arrays are the same
            # if they are the same then we return True, otherwise False.

            # we could use a hashmap to figure this out as well.  
            hashMapS = {}
            hashMapT = {}
            
            for i in s:
                if i in hashMapS:
                    hashMapS[i] += 1
                else: 
                    hashMapS[i] = 1

            for j in t:
                if j in hashMapT:
                    hashMapT[j] += 1
                else: 
                    hashMapT[j] = 1
            return hashMapS == hashMapT