#!/usr/bin/python3.11

numbers = [5, 3, 8, 3, 1, 5, 9, 2, 8]

unique_numbers=list(set(numbers))
numbers_tuple=tuple(unique_numbers)
min_num=min(numbers_tuple)
max_num=max(numbers_tuple)

print("Original list:", numbers)
print("Tuple without duplicates:", numbers_tuple)
print("Minimum number:", min_num)
print("Maximum number:", max_num)