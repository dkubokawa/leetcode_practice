# LC 76 (Hard): Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Variable-Length Sliding Window
        # Time-Complexity: O(n) where n is the length of s
        # Space-Complexity: O(m) is the total number of unique characters in t or s, whichever is greater
        if not s or not t:
            return ""

        # Use dictionary to track character frequencies
        count_t = {}
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        # Result tracking vars
        need = len(count_t)
        found = 0
        result_l_idx = None
        result_r_idx = None
        min_window = float('inf')  # Need inf so any valid window is less than it

        # Window variables
        start = 0
        state = {}

        for end in range(len(s)):
            # Expand window
            curr_char = s[end]
            state[curr_char] = 1 + state.get(curr_char, 0)

            # To check we have found all the chars in a window must have the same count
            if curr_char in count_t and state[curr_char] == count_t[curr_char]:
                found += 1

            # Once we have found chars == need chars, we have a valid window
            while found == need:
                start_char = s[start]

                # Update result if current window is smaller
                if end - start + 1 < min_window:
                    min_window = end - start + 1
                    result_l_idx = start
                    result_r_idx = end

                # Contract window
                state[start_char] -= 1
                # Do not have a count match for the character anymore
                if start_char in count_t and state[start_char] < count_t[start_char]:
                    found -= 1
                start += 1

        return "" if min_window == float('inf') else s[result_l_idx: result_r_idx + 1]