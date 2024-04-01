from src.sols import contains_duplicate
from src.sols import valid_anagram
from src.sols import two_sum
from src.sols import group_anagrams
from src.sols import top_k_frequent
from src.sols import prod_arr_except_self
from src.sols import longest_cons_seq
from src.sols import valid_palindrome

import unittest
import timeout_decorator

class TestSolutions(unittest.TestCase):
    @timeout_decorator.timeout(3)
    def test_contains_duplicate(self):
        self.assertEqual(contains_duplicate.Solution().containsDuplicate([1,2,3,1]), True)
        self.assertEqual(contains_duplicate.Solution().containsDuplicate([1,2,3,4]), False)
        self.assertEqual(contains_duplicate.Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)
        self.assertEqual(contains_duplicate.Solution().containsDuplicate([1,2,3,4,5,6,7,8,9,10]), False)
        
    @timeout_decorator.timeout(3)
    def test_valid_anagram(self):
        self.assertEqual(valid_anagram.Solution().isAnagram("anagram", "nagaram"), True)
        self.assertEqual(valid_anagram.Solution().isAnagram("rat", "car"), False)
        self.assertEqual(valid_anagram.Solution().isAnagram("a", "ab"), False)
        self.assertEqual(valid_anagram.Solution().isAnagram("a", "a"), True)
        
    @timeout_decorator.timeout(3)
    def test_two_sum(self):
        self.assertEqual(two_sum.Solution().twoSum([2,7,11,15], 9), [0, 1])
        self.assertEqual(two_sum.Solution().twoSum([3,2,4], 6), [1, 2])
        self.assertEqual(two_sum.Solution().twoSum([3,3], 6), [0, 1])
        
    @timeout_decorator.timeout(3)
    def test_group_anagrams(self):
        self.assertEqual(group_anagrams.Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [["eat","tea","ate"],["tan","nat"],["bat"]])
        self.assertEqual(group_anagrams.Solution().groupAnagrams(["a"]), [["a"]])
        self.assertEqual(group_anagrams.Solution().groupAnagrams([""]), [[""]])
        
    @timeout_decorator.timeout(3)
    def test_top_k_frequent(self):
        self.assertEqual(top_k_frequent.Solution().topKFrequent([1,1,1,2,2,3], 2), [1, 2])
        self.assertEqual(top_k_frequent.Solution().topKFrequent([1], 1), [1])
        self.assertEqual(top_k_frequent.Solution().topKFrequent([1,2,3,4,5,6,7,8,9,10], 10), [1,2,3,4,5,6,7,8,9,10])
        
    @timeout_decorator.timeout(3)
    def test_prod_arr_except_self(self):
        self.assertEqual(prod_arr_except_self.Solution().productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(prod_arr_except_self.Solution().productExceptSelf([1,2,3,4,5]), [120,60,40,30,24])
        self.assertEqual(prod_arr_except_self.Solution().productExceptSelf([1,2,3,4,5,6]), [720,360,240,180,144,120])
        
    @timeout_decorator.timeout(3)
    def test_longest_cons_seq(self):
        self.assertEqual(longest_cons_seq.Solution().longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(longest_cons_seq.Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)
        self.assertEqual(longest_cons_seq.Solution().longestConsecutive([1,2,0,1]), 3)
        
    @timeout_decorator.timeout(3)
    def test_valid_palindrome(self):
        self.assertEqual(valid_palindrome.Solution().isPalindrome("ada"), True)
        self.assertEqual(valid_palindrome.Solution().isPalindrome("adaa"), False)
        self.assertEqual(valid_palindrome.Solution().isPalindrome("adaada"), True)
                         
                         
if __name__ == '__main__':
    unittest.main()