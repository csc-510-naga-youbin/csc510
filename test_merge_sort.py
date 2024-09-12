from hw2_debugging import merge_sort

def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == expected

def test_empty_list():
    arr = []
    expected = []
    assert merge_sort(arr) == expected

def test_reverse_sorted_list():
    arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == expected

def test_same_element_list():
    arr = [7, 7, 7, 7, 7]
    expected = [7, 7, 7, 7, 7]
    assert merge_sort(arr) == expected

def test_list_with_duplicates():
    arr = [4, 2, 5, 2, 3, 4, 1]
    expected = [1, 2, 2, 3, 4, 4, 5]
    assert merge_sort(arr) == expected
I quickly wrote test cases.
def test_unsorted_array():
    arr = [5, 3, 1, 4, 2]
    expected = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == expected
