class Solution:
    def isValid(self, s: str) -> bool:
        """Return whether every opening bracket is correctly closed."""
        opening_for = {")": "(", "]": "[", "}": "{"}
        stack = []

        for bracket in s:
            if bracket in opening_for.values():
                stack.append(bracket)
            elif not stack or stack.pop() != opening_for.get(bracket):
                return False

        return not stack
