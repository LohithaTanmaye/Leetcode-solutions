import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
for folder in ("arrays-strings", "basic-algorithms", "stacks"):
    sys.path.insert(0, str(ROOT / folder))

from best_time_to_buy_and_sell_stock import Solution as StockSolution
from binary_search import Solution as BinarySearchSolution
from longest_common_prefix import Solution as PrefixSolution
from move_zeroes import Solution as MoveZeroesSolution
from reverse_string import Solution as ReverseStringSolution
from two_sum import Solution as TwoSumSolution
from valid_anagram import Solution as AnagramSolution
from valid_parentheses import Solution as ParenthesesSolution


class TwoSumTests(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(TwoSumSolution().twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_duplicate_values(self):
        self.assertEqual(TwoSumSolution().twoSum([3, 3], 6), [0, 1])

    def test_no_matching_pair(self):
        with self.assertRaises(ValueError):
            TwoSumSolution().twoSum([1, 2, 3], 10)


class ReverseStringTests(unittest.TestCase):
    def test_normal_case(self):
        chars = list("hello")
        self.assertIsNone(ReverseStringSolution().reverseString(chars))
        self.assertEqual(chars, list("olleh"))

    def test_empty_list(self):
        chars = []
        ReverseStringSolution().reverseString(chars)
        self.assertEqual(chars, [])


class ValidAnagramTests(unittest.TestCase):
    def test_normal_case(self):
        self.assertTrue(AnagramSolution().isAnagram("anagram", "nagaram"))

    def test_empty_strings(self):
        self.assertTrue(AnagramSolution().isAnagram("", ""))


class StockTests(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(StockSolution().maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_prices_only_decrease(self):
        self.assertEqual(StockSolution().maxProfit([7, 6, 4, 3, 1]), 0)

    def test_empty_prices(self):
        self.assertEqual(StockSolution().maxProfit([]), 0)


class LongestCommonPrefixTests(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(
            PrefixSolution().longestCommonPrefix(["flower", "flow", "flight"]),
            "fl",
        )

    def test_empty_list(self):
        self.assertEqual(PrefixSolution().longestCommonPrefix([]), "")


class BinarySearchTests(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(BinarySearchSolution().search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_empty_list(self):
        self.assertEqual(BinarySearchSolution().search([], 5), -1)


class MoveZeroesTests(unittest.TestCase):
    def test_normal_case(self):
        nums = [0, 1, 0, 3, 12]
        self.assertIsNone(MoveZeroesSolution().moveZeroes(nums))
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_all_zeroes(self):
        nums = [0, 0, 0]
        MoveZeroesSolution().moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0])


class ValidParenthesesTests(unittest.TestCase):
    def test_normal_case(self):
        self.assertTrue(ParenthesesSolution().isValid("{[]}"))

    def test_empty_string(self):
        self.assertTrue(ParenthesesSolution().isValid(""))


if __name__ == "__main__":
    unittest.main()
