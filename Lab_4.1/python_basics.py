# hello world
print("hello world!")

# variables
empty_variable = None
some_text = "Python"
single_full_number = 42
single_fractional_number = 3.41
list_of_numbers = [1, 2, 3, 0, -5, single_full_number]

print(empty_variable)
print(some_text, list_of_numbers)

# loops
for number in list_of_numbers:
    incremented_number = number + 1
    print(number, incremented_number)
print("loop finished")

# conditionals
if some_text == "Python":
    print(some_text + " is easy to learn!")

for number in list_of_numbers:
    if number > 1:
        print(number, " greater than 1")
    elif number < 1:
        print(number, " smaller than 1")
    else:
        print(number, " it is 1!!")

