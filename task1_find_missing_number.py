def find_missing_number(arr: list) -> int:
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

if __name__ == "__main__":
    arr = [3, 0, 1]
    print("Missing number is:", find_missing_number(arr))  # Output: 2
