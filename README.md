# List Processing Assignment

In this assignment, you will implement three functions that process lists of numbers in different ways. Each function has its own specific requirements and test cases.

## Functions to Implement

### 1. find_peaks(numbers)
- Find all peak values in a list of numbers
- A peak is a number that is greater than both its left and right neighbors
- Return the peaks in the order they appear
- Example: find_peaks([1, 3, 2, 3, 5, 3]) returns [3, 5]

### 2. running_average(numbers, window_size)
- Calculate the running average using a sliding window
- Round results to 2 decimal places
- Raise ValueError if window_size is larger than the list or if list is empty
- Example: running_average([1, 2, 3, 4, 5], 3) returns [2.0, 3.0, 4.0]

### 3. find_duplicates(numbers)
- Find all numbers that appear more than once
- Return them in ascending order
- Example: find_duplicates([1, 2, 2, 3, 3, 3, 4]) returns [2, 3]

## Testing Your Code
- Run tests using pytest: `pytest tests/`
- All tests must pass for full credit
- Pay attention to edge cases and error handling

## Submission
- Complete the functions in src/assignment.py
- Do not modify the test files
- Push your changes to GitHub
- Verify that all tests pass in the GitHub Actions workflow
