# Leetcode Practice

## General Code Templates
* Variable Length Sliding Window
* Fixed Length Sliding Window

### Variable Length Sliding Window
#### Approach: O(N)
* Try to make a single pass through the entire array using a sliding window
* Use the diff <code>end - start + 1</code> as window length. Need the <code>+1</code> since if <code>end = start</code> then we have window length of 1
```python
def variable_length_sliding_window(nums):
    state = # Appropriate data structure
    start = 0
    max_window = 0

    for end in range(len(nums)):
        
        # extend window by adding nums[end] to state in O(1) in time 

        if or while state is not valid:
            # contract window until it is valid again by removing nums[start] from state in O(1) in time
            # then update start
            start += 1

        # Once valid, update max
        max_window = max(max_window, end - start + 1)
    return max_window
```

### Fixed Length Sliding Window
#### Approach: O(N)
* Try to make a single pass through the entire array using a sliding window
* Use the diff <code>end - start + 1</code> as window length. Need the <code>+1</code> since if <code>end = start</code> then we have window length of 1
```python
def fixed_length_sliding_window(nums, k):
    state = # choose appropriate data structure
    start = 0
    max_window = 0

    for end in range(len(nums)):
        # extend window by adding nums[end] to state in O(1) in time
	 
        # window size = k
        if end - start + 1 == k:
            # update max (might need an if-statement)
            max_window = max(max_window, state)

            # contract window by removing nums[start] from state in O(1) in time
            # then update start
            start += 1

    return max_window 
```