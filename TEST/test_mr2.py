import pytest
import sys
import os
from test_cases_mr2 import test_cases

# Adjust the import path to the SUT (System Under Test)
original_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../SUT'))
sys.path.insert(0, original_dir)

from merge_sort import merge_sort

def test_mr2():
    """ Test MR2: Verify the commutative property of sorting """
    for first_list, second_list in test_cases:
        # Sort the concatenated input
        concatenated_input = first_list + second_list
        sorted_concatenated = merge_sort(concatenated_input)

        # Sort each list individually and concatenate the results
        sorted_first = merge_sort(first_list)
        sorted_second = merge_sort(second_list)
        sorted_combined = sorted_first + sorted_second

        # Check if both sorted outputs match
        assert sorted_concatenated == sorted_combined, (
            f"MR2 failed for first_list={first_list} and second_list={second_list}. "
            f"Sorted concatenated: {sorted_concatenated}, "
            f"Sorted individual + concatenated: {sorted_combined}"
        )
        print(f"MR2 succeeded for first_list={first_list} and second_list={second_list}.")

def get_mr_outputs():
    """ Return expected outputs for MR2 test cases """
    expected_outputs = []
    for first_list, second_list in test_cases:
        # Sort each list individually and concatenate the results
        sorted_first = merge_sort(first_list)
        sorted_second = merge_sort(second_list)
        expected_output = sorted_first + sorted_second
        expected_outputs.append(expected_output)
    return expected_outputs

if __name__ == "__main__":
    test_mr2()

    # Print expected outputs for MR2
    expected_outputs = get_mr_outputs()
    for case, output in zip(test_cases, expected_outputs):
        first_list, second_list = case
        print(f"Expected output for first_list={first_list} and second_list={second_list}: {output}")
