from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the plan of action here is create a hash map. 
        # hash map can count the occurences of the number. 

        # Question: is the list sorted? 
        count = {}
        # this is our sublist with the actual number with its count.
        freq = [[] for i in range(len(nums) + 1)] 
        
        for n in nums:
            if n in count:
                count[n] += 1 
            else: 
                count[n] = 1
        # .items() returns the key value pairs. 
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        # run foor loop in desecending order.
        # 0, -1 will do it. 
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        
            


