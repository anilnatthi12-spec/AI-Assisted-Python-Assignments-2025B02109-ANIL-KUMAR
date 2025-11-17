list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = sum(num for num in list_num if num % 2 == 0)
odd_sum = sum(num for num in list_num if num % 2 != 0)

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")


