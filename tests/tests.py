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
from src import valid_parenthesis
from src import search_rot_sort_array
from src import min_rot_sort_array

import sys
import unittest
import inspect
import timeout_decorator
from typing import Generator


class TestSolutions(unittest.TestCase):
    @staticmethod
    def method_gettr(
        problem, f_filter=lambda *args, **kwargs: True
    ) -> Generator[callable, None, None]:
        """
        Get all methods from the problem class that pass the filter function.
        """
        for _, method in inspect.getmembers(
            problem, predicate=lambda func: inspect.isfunction(func) and f_filter(func)
        ):
            yield method

    def data_func(self, inout, problem, f_filter=lambda *args, **kwargs: True):
        """
        Test the methods from the problem class with the given input/output pairs.
        """
        for data, expected in inout:
            for method in TestSolutions.method_gettr(problem, f_filter):
                try:
                    self.assertEqual(method(problem(), *data), expected)
                except AssertionError as e:
                    print(f"Method: {method.__name__} failed on input: {data}")
                    raise e

    @timeout_decorator.timeout(3)
    def test_contains_duplicate(self):
        self.data_func(
            [
                ([[1, 2, 3, 1]], True),
                ([[1, 2, 3, 4]], False),
                ([[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]], True),
                ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], False),
            ],
            contains_duplicate.Solution,
        )

    @timeout_decorator.timeout(3)
    def test_valid_anagram(self):
        self.data_func(
            [
                (["anagram", "nagaram"], True),
                (["rat", "car"], False),
                (["a", "ab"], False),
                (["a", "a"], True),
            ],
            valid_anagram.Solution
        )

    @timeout_decorator.timeout(3)
    def test_two_sum(self):
        self.data_func(
            [
                ([[2, 7, 11, 15], 9], [0, 1]),
                ([[3, 2, 4], 6], [1, 2]),
                ([[3, 3], 6], [0, 1]),
            ],
            two_sum.Solution
        )

    @timeout_decorator.timeout(3)
    def test_group_anagrams(self):
        self.data_func(
            [
                ([["eat", "tea", "tan", "ate", "nat", "bat"]], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
                ([["a"]], [["a"]]),
                ([[""]], [[""]]),
            ],
            group_anagrams.Solution
        )

    @timeout_decorator.timeout(3)
    def test_top_k_frequent(self):
        self.data_func(
            [
                ([[1, 1, 1, 2, 2, 3], 2], [1, 2]),
                ([[1], 1], [1]),
                ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ],
            top_k_frequent.Solution,
            lambda func: func.__name__ == "topKFrequent"
        )

    @timeout_decorator.timeout(3)
    def test_prod_arr_except_self(self):
        self.data_func(
            [
                ([[1, 2, 3, 4]], [24, 12, 8, 6]),
                ([[1, 2, 3, 4, 5]], [120, 60, 40, 30, 24]),
                ([[1, 2, 3, 4, 5, 6]], [720, 360, 240, 180, 144, 120]),
            ],
            prod_arr_except_self.Solution
        )

    @timeout_decorator.timeout(3)
    def test_longest_cons_seq(self):
        self.data_func(
            [
                ([[100, 4, 200, 1, 3, 2]], 4),
                ([[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], 9),
                ([[1, 2, 0, 1]], 3),
            ],
            longest_cons_seq.Solution
        )

    @timeout_decorator.timeout(3)
    def test_valid_palindrome(self):
        self.data_func(
            [
                (["ada"], True),
                (["adaa"], False),
                (["adaada"], True),
            ],
            valid_palindrome.Solution
        )

    @timeout_decorator.timeout(3)
    def test_most_water_container(self):
        self.data_func(
            [
                ([[1, 8, 6, 2, 5, 4, 8, 3, 7]], 49),
                ([[1, 1]], 1),
                ([[4, 3, 2, 1, 4]], 16),
            ],
            most_water_container.Solution
        )

    @timeout_decorator.timeout(3)
    def test_longest_rep_char_replacement(self):
        self.data_func(
            [
                (["ABAB", 2], 4),
                (["AABABBA", 1], 4),
                (["A", 1], 1),
            ],
            longest_rep_char_replacement.Solution
        )

    @timeout_decorator.timeout(3)
    def test_longest_subs_no_repeat(self):
        self.data_func(
            [
                (["abcabcbb"], 3),
                (["bbbbb"], 1),
                (["pwwkew"], 3),
            ],
            longest_subs_no_repeat.Solution
        )

    @timeout_decorator.timeout(3)
    def test_minimum_window_substring(self):
        self.data_func(
            [
                (["ADOBECODEBANC", "ABC"], "BANC"),
                (["a", "a"], "a"),
                (["a", "aa"], ""),
            ],
            minimum_window_substring.Solution
        )
        

    @timeout_decorator.timeout(3)
    def test_valid_parenthesis(self):
        self.data_func(
            [
                (["()"], True),
                (["()[]{}"], True),
                (["(]"], False),
                (["([)]"], False),
                (["{[]}"], True),
            ],
            valid_parenthesis.Solution
        )

    @timeout_decorator.timeout(3)
    def test_search_rot_sort_array(self):
        self.data_func(
            [
                ([[4, 5, 6, 7, 0, 1, 2], 0], 4),
                ([[4, 5, 6, 7, 0, 1, 2], 3], -1),
                ([[1], 0], -1),
            ], 
            search_rot_sort_array.Solution
        )

    @timeout_decorator.timeout(3)
    def test_min_rot_sort_array(self):
        self.data_func(
            [
                ([[3, 4, 5, 1, 2]], 1),
                ([[4, 5, 6, 7, 0, 1, 2]], 0),
                ([[11, 13, 15, 17]], 11),
                ([[3, 1, 2]], 1),
            ],
            min_rot_sort_array.Solution
        )


if __name__ == "__main__":
    unittest.main()
