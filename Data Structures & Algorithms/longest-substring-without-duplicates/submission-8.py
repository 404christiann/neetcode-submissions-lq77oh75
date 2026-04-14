class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        charSet = set()
        for right in range(len(s)):
            while s[right] in charSet: 
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            # Think of maxLength as your Personal Best 
            # and right - left + 1 as your Current Score.
            # maxLength is the top number we've see thus far and right - left + 1 is the current 
            # length of the substring.
            maxLength = max(maxLength, right - left + 1)
        return maxLength 
        

