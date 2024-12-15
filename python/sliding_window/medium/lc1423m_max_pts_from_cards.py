# LC 1423 (Medium): Maximum Points You Can Obtain from Cards

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Trick here is we can "discard" n - k cards
        # i.e. for cardPoints = [1,2,3,4,5,6,7], k = 3
        # our valid hands are [1,2,3], [1,6,7], [1,2,7], [5,6,7]
        # so we discard a sliding window of length n - k = 4 cards
        # Time-Complexity: O(N)
        # Space-Complexity: O(1)

        total = sum(cardPoints)
        n = len(cardPoints)
        if k >= n:
            return total

        start = 0
        state = 0
        max_window = 0
        for end in range(n):
            state += cardPoints[end]

            if end - start + 1 == n - k:
                max_window = max(max_window, total - state)
                state -= cardPoints[start]
                start += 1

        return max_window