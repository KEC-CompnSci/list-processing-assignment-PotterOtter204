import math
"""
List Processing Assignment

This assignment focuses on list manipulation and data processing in Python.
You will implement functions to process lists of numbers using various algorithms.
"""

def find_peaks(numbers):
    """
    Find all peak values in a list of numbers. A peak is a number that is greater
    than both its left and right neighbors.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        list: A list of peak values in the order they appear
        
    Example:
        find_peaks([1, 3, 2, 3, 5, 3]) -> [3, 5]
    """
    length = len(numbers)
    peaks = []
    for i in range(length):
        if i > 0 and i < length-1:
            val = numbers[i]
            if val > numbers[i-1] and val > numbers[i+1]:
                peaks.append(val)

    return peaks



def running_average(numbers, window_size):
    """
    Calculate the running average for a list of numbers using the specified window size.
    
    Args:
        numbers (list): A list of numbers
        window_size (int): The size of the moving window
        
    Returns:
        list: A list of running averages, rounded to 2 decimal places
        
    Example:
        running_average([1, 2, 3, 4, 5], 3) -> [2.0, 3.0, 4.0]
    """
    length = len(numbers)
    i = 0
    averages = []

    if window_size > length:
        raise ValueError("window size too big")
    while i <= length -window_size:
        slice = numbers[i: i + window_size]
        answer = sum(slice)/window_size
        answer = round(answer, 2)
        averages.append(answer)
        i += 1
    return averages

def find_duplicates(numbers):
    """
    Find all numbers that appear more than once in the list.
    Return them in ascending order.
    
    Args:
        numbers (list): A list of numbers
        
    Returns:
        list: A sorted list of numbers that appear multiple times
        
    Example:
        find_duplicates([1, 2, 2, 3, 3, 3, 4]) -> [2, 3]
    """
    numDict = {}
    duplicates = []
    for num in numbers:
        if num not in numDict:
            numDict[num] = 1
        else:
            
            if numDict[num] ==1:
                duplicates.append(num)
            numDict[num] +=1
    return duplicates
