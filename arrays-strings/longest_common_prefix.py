from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Return the longest prefix shared by every string."""
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            common_length = 0
            limit = min(len(prefix), len(word))
            while (
                common_length < limit
                and prefix[common_length] == word[common_length]
            ):
                common_length += 1

            prefix = prefix[:common_length]
            if not prefix:
                break

        return prefix
