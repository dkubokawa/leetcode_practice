# LC 567 (Medium): Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fixed-Length Sliding Window
        # Time-Complexity: O(n)
        # Space-Complexity: O(2n) = O(n) using arrays
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1

        start = 0
        for end in range(len(s2)):
            s2_count[ord(s2[end]) - ord('a')] += 1

            if end - start + 1 == len(s1):
                if s1_count == s2_count:
                    return True
                s2_count[ord(s2[start]) - ord('a')] -= 1
                start += 1
        return False

    def checkInclusion1(self, s1: str, s2: str) -> bool:
        # Fixed-Length Sliding Window
        # Time-Complexity: O(n)
        # Space-Complexity: O(2n) = O(n) because we use 2 hashmaps

        if len(s1) > len(s2):
            return False

        char_s1 = {}
        for value in s1:
            char_s1[value] = 1 + char_s1.get(value, 0)

        start = 0
        state = {}
        for end in range(len(s2)):
            state[s2[end]] = 1 + state.get(s2[end], 0)

            if end - start + 1 == len(s1):
                if state == char_s1:
                    return True
                state[s2[start]] -= 1
                if state[s2[start]] == 0:
                    del state[s2[start]]
                start += 1
        return False

