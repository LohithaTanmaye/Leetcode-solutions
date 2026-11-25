
# LeetCode Solutions

**Name:** Kuppala Lohitha Tanmaye  
**SRN:** R25EQ037  
**Course:** Portfolio Building  
**Activity:** Activity 6 – LeetCode Practice & Portfolio Integration  
**Program:** BTech – Information Science and Engineering (ISE)  
**Semester:** 3rd Semester

Personal LeetCode practice portfolio for B25GE0101.

## Table of Contents

1. [Arrays and Strings](./arrays-strings/)
2. [Basic Algorithms](./basic-algorithms/)
3. [Stacks](./stacks/)
4. [Linked Lists](./linked-lists/)
5. [Progress Tracker](./PROGRESS.md)

## About This Repository

This repository contains eight Python solutions to LeetCode problems. Each
solution uses the expected LeetCode `Solution` class and method signature.
Local tests are kept separate from the submission-ready solution files.

## Solutions and Complexity

### Arrays and Strings

| Problem | Approach | Time | Space | Solution |
|---|---|---|---|---|
| Two Sum | Store seen values and look up each complement | O(n) | O(n) | [two_sum.py](./arrays-strings/two_sum.py) |
| Reverse a String | Swap characters from both ends in place | O(n) | O(1) | [reverse_string.py](./arrays-strings/reverse_string.py) |
| Valid Anagram | Compare sorted character sequences | O(n log n) | O(n) | [valid_anagram.py](./arrays-strings/valid_anagram.py) |
| Best Time to Buy and Sell Stock | Track the lowest price and best profit so far | O(n) | O(1) | [best_time_to_buy_and_sell_stock.py](./arrays-strings/best_time_to_buy_and_sell_stock.py) |
| Longest Common Prefix | Compare matching characters across each word | O(S) | O(m) | [longest_common_prefix.py](./arrays-strings/longest_common_prefix.py) |

### Basic Algorithms

| Problem | Approach | Time | Space | Solution |
|---|---|---|---|---|
| Binary Search | Halve the sorted search range each step | O(log n) | O(1) | [binary_search.py](./basic-algorithms/binary_search.py) |
| Move Zeroes | Move non-zero values forward in place | O(n) | O(1) | [move_zeroes.py](./basic-algorithms/move_zeroes.py) |

### Stacks

| Problem | Approach | Time | Space | Solution |
|---|---|---|---|---|
| Valid Parentheses | Match closing brackets against a stack | O(n) | O(n) | [valid_parentheses.py](./stacks/valid_parentheses.py) |

`n` is the input size; for Longest Common Prefix, `S` is the total number of
characters and `m` is the length of the shortest input string.

## Run the Tests

From the repository root, run:

```bash
python -m unittest discover -s tests -v
```

The test suite includes normal and edge cases for all eight solutions. The
`linked-lists` folder is included for future practice; no linked-list problem
is part of this activity.
