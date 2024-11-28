class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            if char in char_map:
                if len(stack) == 0 or stack.pop() != char_map[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
