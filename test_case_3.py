from hw2_debugging import merge_sort

def test_array_with_duplicates():
    arr = [4, 2, 4, 3, 1, 2]
    expected = [1, 2, 2, 3, 4, 4]
    assert merge_sort(arr) == expected
