from hw2_debugging import merge_sort

def test_unsorted_array():
    arr = [5, 3, 1, 4, 2]
    expected = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == expected
