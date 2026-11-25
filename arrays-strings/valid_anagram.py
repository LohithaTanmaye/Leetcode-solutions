class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Return whether t is an anagram of s."""
        return sorted(s) == sorted(t)
