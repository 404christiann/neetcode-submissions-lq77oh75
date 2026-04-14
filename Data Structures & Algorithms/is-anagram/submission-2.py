class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            # we should use a hashmap to figure this out
            # hashmap will lower the time complexity of this problem to O(n+m)
            

            hashMapS = {}
            hashMapT = {}
            if len(s) != len(t):
                return False
            
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