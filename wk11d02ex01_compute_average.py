def computeAverage(numbers):
    total = 0
    count = 0

    for num in numbers:
        if num == 0:
            continue
        else:
            total += num
            count += 1
            return total / count

    if count == 0:
        return None
    return total / count
