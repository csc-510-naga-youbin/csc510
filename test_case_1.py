from hw2_debugging import merge_sort

def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == expected
