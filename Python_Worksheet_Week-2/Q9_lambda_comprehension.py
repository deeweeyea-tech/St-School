numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [n ** 2 for n in numbers]
print("Squares:", squares)

evens = list(filter(lambda n: n % 2 == 0, numbers))
print("Even Numbers:", evens)