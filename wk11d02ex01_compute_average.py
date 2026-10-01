def computeAverage(numbers):
    """Return the average of numbers before the first 0 sentinel."""
    total = 0
    count = 0

    # Process numbers from left to right.
    for num in numbers:
        # Stop when the sentinel value is reached.
        if num == 0:
            break
        else:
            # Include this number in the running total and count.
            total = total + num
            count = count + 1

    # Avoid division by zero when no numbers were processed.
    if count == 0:
        return 0.0
    else:
        average = total / count
        return average


# Test the function using the four arrays from the lesson.
if __name__ == "__main__":
    test_cases = [
        [22, 9, 0, 17],
        [22, 0, 49, 8],
        [35, 13, 22, 0],
        [10, 5, -4, 27],
    ]

    for numbers in test_cases:
        result = computeAverage(numbers)
        print(f"Numbers: {numbers}")
        print(f"Computed average: {result}")
        print()

