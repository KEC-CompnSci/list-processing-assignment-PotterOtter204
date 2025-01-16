# tests/test_assignment.py
import pytest
from src.assignment import find_peaks, running_average, find_duplicates

def test_find_peaks():
    assert find_peaks([1, 3, 2, 3, 5, 3]) == [3, 5]
    assert find_peaks([1, 2, 3, 4, 5]) == []
    assert find_peaks([5, 4, 3, 2, 1]) == []
    assert find_peaks([1, 2, 1, 2, 1]) == [2, 2]
    assert find_peaks([]) == []
    assert find_peaks([1]) == []
    assert find_peaks([1, 2]) == []

def test_running_average():
    assert running_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]
    assert running_average([2, 4, 6, 8], 2) == [3.0, 5.0, 7.0]
    assert running_average([1], 1) == [1.0]
    assert running_average([1, 2, 3], 3) == [2.0]
    with pytest.raises(ValueError):
        running_average([1, 2, 3], 4)
    with pytest.raises(ValueError):
        running_average([], 1)

def test_find_duplicates():
    assert find_duplicates([1, 2, 2, 3, 3, 3, 4]) == [2, 3]
    assert find_duplicates([1, 2, 3, 4]) == []
    assert find_duplicates([1, 1, 1, 1]) == [1]
    assert find_duplicates([]) == []
    assert find_duplicates([3, 1, 2, 1, 3]) == [1, 3]
