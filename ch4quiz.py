#1. tell whehter the natural number is odd or even using the funtion is_odd.
# def is_odd(number):
#     if number % 2 == 0:
#         print("this is even number")
#         return True
#     else:
#         print("this is odd number")
#         return False

# print(is_odd(10))

# #2.
# def get_avg(*num):
#     result = 0
#     for i in num:
#         result += i
#     return result / len(num)

# print(get_avg(2,3,4,5))

# #3.
# input1 = input("input the first number: ")
# input2 = input("input the second number: ")

# total = int(input1) + int(input2)
# print(total)

#4.
user_input = input("Enter your age: ")
try:
    value = int(user_input)
    print("Input is an integer number", value)
except ValueError:
    try:
        value = float(user_input)
        print("this is float number", value)
    except ValueError:
        print("this is string, not a number")
