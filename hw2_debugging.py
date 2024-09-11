"""
Module for sorting an array using merge sort algorithm.
"""

import random


def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Recombines two sorted arrays into a single sorted array.

    Args:
        left_arr (list): The left sorted array.
        right_arr (list): The right sorted array.

    Returns:
        list: The merged sorted array.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + i] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[right_index + i] = left_arr[i]

    return merge_arr


if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(20)]
    arr_out = merge_sort(arr)
    print(arr_out)