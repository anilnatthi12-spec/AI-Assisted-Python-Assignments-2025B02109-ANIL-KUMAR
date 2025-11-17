"""Find largest number in a list — iterative and builtin versions with tests.

This module provides two implementations for finding the largest element in a
list of comparable elements and a small test harness that runs when executed
directly.

Functions:
  - find_max_iterative(lst): iterative O(n) scan
  - find_max_builtin(lst): uses Python's built-in max()

Both functions validate input and raise clear exceptions for invalid input.
"""

from typing import Any, List


def find_max_iterative(lst: List[Any]) -> Any:
    """
    Return the largest element in `lst` using an iterative scan.

    Args:
        lst: list of comparable items (e.g., numbers)

    Returns:
        The maximum element from the list.

    Raises:
        TypeError: if `lst` is not a list.
        ValueError: if `lst` is empty.

    Complexity: O(n) time, O(1) extra space.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("Cannot find max of an empty list")

    # Initialize with first element and iterate once through the rest
    max_val = lst[0]
    for item in lst[1:]:
        # Relies on Python comparison; TypeError will be raised if items are
        # not comparable (e.g., mixing str and int)
        if item > max_val:
            max_val = item
    return max_val


def find_max_builtin(lst: List[Any]) -> Any:
    """
    Return the largest element in `lst` using Python's built-in `max()`.

    Args and exceptions are the same as for `find_max_iterative`.

    Complexity: O(n) time, O(1) extra space (ignoring iterator overhead).
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("Cannot find max of an empty list")
    return max(lst)


def _run_tests() -> None:
    """Simple tests to verify correctness of the implementations."""
    tests = [
        ([3, 1, 4, 2], 4),
        ([-5, -1, -3], -1),
        ([0], 0),
        ([1.5, 2.5, 0.5], 2.5),
    ]

    for lst, expected in tests:
        it = find_max_iterative(lst)
        bi = find_max_builtin(lst)
        assert it == expected, f"iterative failed for {lst}: got {it}, want {expected}"
        assert bi == expected, f"builtin failed for {lst}: got {bi}, want {expected}"

    # Test behavior on invalid inputs
    try:
        find_max_iterative([])
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for empty list (iterative)")

    try:
        find_max_builtin([])
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for empty list (builtin)")

    print("All tests passed.")


if __name__ == "__main__":
    # Example usage and quick interactive demo
    print("find_max demo — running unit tests...")
    _run_tests()

    # Interactive example: accept a comma-separated list of numbers
    raw = input("Enter numbers separated by commas (or press Enter to skip): ")
    if raw.strip():
        try:
            items = [float(x.strip()) for x in raw.split(",") if x.strip()]
            # Convert floats that are integers to int for nicer printing
            items = [int(x) if x.is_integer() else x for x in items]
            print("Largest (iterative):", find_max_iterative(items))
            print("Largest (builtin):   ", find_max_builtin(items))
        except ValueError:
            print("Could not parse input into numbers. Please enter numeric values.")
