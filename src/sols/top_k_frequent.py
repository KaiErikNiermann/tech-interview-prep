from typing import List
from collections import defaultdict

class Solution(): 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        ### Thought process
        - Place elements into frequency buckets `[index -> [n1, ..., n2]]` where `index` is the frequency of the numbers and `[n1, ..., n2]` are the numbers that have that frequency
        - Return the last k elements
        
        ### Notes 
        - time complexity: $O(n) + O(n) = O(n)$
        - space complexity: $O(2n) = O(n)$
        
        """
        # init bucket and count 
        count = {}
        freq = [[] for _ in range(len(nums) + 1)] 
        
        # count freq then place in bucket
        for n in nums:
            count[n] = count.get(n, 0) + 1 # index -> frequency
        for n, c in count.items():
            freq[c].append(n)              # frequency -> list of numbers
        
        # get k most frequent numbers
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    
    def topKFrequentCompact(self, nums: List[int], k: int) -> List[int]:
        """
        ### Thought process 
        - We can use a dictionary to store the frequency of each number
        - We can sort the dictionary by the frequency and return the last k elements
        
        ### Notes
        - time complexity: $O(n\\log n)$ 
        - space complexity: $O(n)$
        
        
        > I feel like you could use this in an interview, practically speaking its close to the bucket sort solution, I would probably expand the return value though, either that or kind of just explain it to the interviewer
        """
        m = defaultdict(int)
        for n in nums: 
            m[n] += 1 

        return list(dict(sorted(m.items(), key=lambda item: item[1])).keys())[len(m.keys()) - k:]
