# LC 3 (Medium): Longest Substring Without Repeating Characters

from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: Dict[str, int] = {}
        start = 0
        max_len = 0
        for end in range(len(s)):
            # extend the window
            seen[s[end]] = 1 + seen.get(s[end], 0)

            # state is invalid when we have char of cnt > 2
            while seen[s[end]] > 1:
                # handle by moving the start index so that it is past the point of the left-most duplicate index
                seen[s[start]] -= 1
                start += 1

            # know the state is valid, can update the max-length now
            # Compare to the current window length or end - start + 1
            max_len = max(max_len, end - start + 1)
        return max_len

