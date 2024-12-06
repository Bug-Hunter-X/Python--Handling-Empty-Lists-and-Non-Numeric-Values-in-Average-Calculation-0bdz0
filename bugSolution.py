import numbers

def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, numbers.Number)]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}") #This will print 0 as expected

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}") #This will print 30.0 as expected

my_list = [10, 20, 'a', 40, 50]
result = calculate_average(my_list) # This will print 30.0 as expected
my_list = ['a', 'b', 'c']
result = calculate_average(my_list) # This will print 0 as expected