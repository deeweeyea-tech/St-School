def separate_even_odd(numbers):
    even_list = []
    odd_list = []

    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return (even_list, odd_list)


print(separate_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))