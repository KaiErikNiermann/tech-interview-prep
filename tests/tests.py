from src import contains_duplicate
from src import valid_anagram
from src import two_sum
from src import group_anagrams
from src import top_k_frequent
from src import prod_arr_except_self
from src import longest_cons_seq
from src import valid_palindrome
from src import most_water_container
from src import longest_rep_char_replacement
from src import longest_cons_seq
from src import longest_subs_no_repeat
from src import minimum_window_substring

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
        
    @timeout_decorator.timeout(3)
    def test_most_water_container(self):
        self.assertEqual(most_water_container.Solution().maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(most_water_container.Solution().maxArea([1,1]), 1)
        self.assertEqual(most_water_container.Solution().maxArea([4,3,2,1,4]), 16)
        
    @timeout_decorator.timeout(3)
    def test_longest_rep_char_replacement(self):
        self.assertEqual(longest_rep_char_replacement.Solution().characterReplacement("ABAB", 2), 4)
        self.assertEqual(longest_rep_char_replacement.Solution().characterReplacement("AABABBA", 1), 4)
        self.assertEqual(longest_rep_char_replacement.Solution().characterReplacement("A", 1), 1)
        
    @timeout_decorator.timeout(3)
    def test_longest_subs_no_repeat(self):
        self.assertEqual(longest_subs_no_repeat.Solution().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(longest_subs_no_repeat.Solution().lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(longest_subs_no_repeat.Solution().lengthOfLongestSubstring("pwwkew"), 3)
                         
                    
    @timeout_decorator.timeout(3)
    def test_minimum_window_substring(self):
        self.assertEqual(minimum_window_substring.Solution().minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(minimum_window_substring.Solution().minWindow("a", "a"), "a")
        self.assertEqual(minimum_window_substring.Solution().minWindow("a", "aa"), "")
                         
if __name__ == '__main__':
    unittest.main()