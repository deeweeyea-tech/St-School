def calculate_statistics(numbers):
    if not numbers:
        return {'mean': 0, 'max': None, 'min': None, 'count': 0}  # Handle empty list case

    # Calculate mean
    mean = sum(numbers) / len(numbers)

    # Calculate max
    maximum = max(numbers)

    # Calculate min
    minimum = min(numbers)

    # calculate count of numbers
    count = len(numbers)
    return {'mean':mean,'max':maximum,'min':minimum,'count':count}


print(calculate_statistics([10, 20, 30, 40, 50]))
print(calculate_statistics([]))