# LC 424 (Medium): Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Implementation:
        1. Use a hashmap to store the number of times a character appears in the window
        2. Use a left and right pointer to keep track of the window
        3. Use a variable to keep track of the most frequent character in the window
        4. If the window is not valid, move the left pointer and decrement the value of the leftmost character
        5. Return the length of the window

        Time Complexity: O(n) since we are iterating through the string once
        Space Complexity: O(26) = O(1) since the hashmap will only contain 26 characters at most
        """

        hashmap_chars = {}
        left = 0
        res = 0

        for right, value in enumerate(s):
            hashmap_chars[value] = 1 + hashmap_chars.get(value, 0)
            most_frequent_char = max(hashmap_chars.values())

            # If it is a non-valid window which occurs when:
            # the window_size (right - left + 1) - most_frequent_char > max_number_replacements
            while (right - left + 1) - most_frequent_char > k:
                # Need to decrement the value of the leftmost pointer and then move the pointer
                hashmap_chars[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
