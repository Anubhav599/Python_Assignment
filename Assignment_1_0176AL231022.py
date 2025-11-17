
"""       PYTHON PRACTICE PROBLEMS - STRUCTURED SOLUTIONS      """         


""" Student Information:
    Name: Anubhav Jain
    Enrollment: 0176AL231022
    Batch: 5
    Batch Time: 10:30 am to 12:10 pm """

"""Description:
    This file contains practice problems covering fundamental Python concepts
    including conditional statements, loops, and problem-solving techniques """
# SECTION 1: BASIC IF-ELSE PROBLEMS


"""
Q1: Check if a number is positive, negative, or zero
"""
# Solution:
# num = int(input("Enter a number: "))
# if num < 0:
#     print("Number is negative!")
# elif num == 0:
#     print("Number is 0!")
# else:
#     print("Number is positive!")

"""
Q2: Check if a number is odd or even
"""
# Solution:
# num = int(input("Enter a number: "))
# if num & 1:
#     print("Number is odd!")
# else:
#     print("Number is even!")

"""
Q3: Check if a year is a leap year
"""
# Solution:
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Year is leap year!")
# else:
#     print("Year is not a leap year!")

"""
Q4: Find the greater of two numbers
"""
# Solution:
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# else:
#     print(f"{num2} is greater than {num1}")

"""
Q5: Check voting eligibility based on age
"""
# Solution:
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible for voting!")
# else:
#     print("You are not eligible for voting")

"""
Q6: Classify a character as vowel or consonant
"""
# Solution:
# ch = input("Enter a single character: ")
# if len(ch) == 1:
#     if ch in "aeiou":
#         print(f"{ch} is a vowel!")
#     else:
#         print(f"{ch} is a consonant!")
# else:
#     print("Please enter a valid single character!")

"""
Q7: Check if a number is divisible by 5
"""
# Solution:
# num = int(input("Enter a number: "))
# if num % 5 == 0:
#     print(f"{num} is divisible by 5!")
# else:
#     print(f"{num} is not divisible by 5!")

"""
Q8: Count the number of digits in a number
"""
# Solution:
# num = int(input("Enter a number: "))
# original_num = num
# digit_count = 0
# while num > 0:
#     num = int(num / 10)
#     digit_count += 1
# print(f"{original_num} has {digit_count} digits!")

"""
Q9: Check if exam is passed (marks >= 40)
"""
# Solution:
# marks = int(input("Enter marks: "))
# if marks >= 40:
#     print("You have passed the exam!")
# else:
#     print("You have not passed the exam!")

"""
Q10: Check if divisible by both 3 and 7 (i.e., divisible by 21)
"""
# Solution:
# num = int(input("Enter a number: "))
# if num % 21 == 0:
#     print(f"{num} is divisible by both 3 and 7!")
# else:
#     print(f"{num} is not a multiple of both 3 and 7!")


# SECTION 2: LADDER IF & NESTED IF PROBLEMS

"""
Q1: Find the greatest of three numbers
"""
# Solution:
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
# if num1 > num2:
#     if num1 > num3:
#         print(f"{num1} is greatest!")
#     else:
#         print(f"{num3} is greatest!")
# else:
#     if num2 > num3:
#         print(f"{num2} is greatest!")
#     else:
#         print(f"{num3} is greatest!")

"""
Q2: Categorize age group
"""
# Solution:
# age = int(input("Enter your age: "))
# if age < 0 or age > 100:
#     print("You should not exist in this multiverse!")
# elif age < 13:
#     print("You are a child!")
# elif age <= 19:
#     print("You are a Teenager!")
# elif age <= 59:
#     print("You are an Adult")
# else:
#     print("You are a Senior")

"""
Q3: Assign grades based on marks
"""
# Solution:
# marks = int(input("Enter marks: "))
# if marks < 0 or marks > 100:
#     print("Invalid marks!")
# elif marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# elif marks >= 35:
#     print("Grade: D")
# else:
#     print("Fail!")

"""
Q4: Classify triangle type
"""
# Solution:
# print("Enter sides of triangle:\n")
# side1 = int(input("Enter side1: "))
# side2 = int(input("Enter side2: "))
# side3 = int(input("Enter side3: "))
# if side1 == side2 and side2 == side3:
#     print("An Equilateral Triangle!")
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("An Isosceles Triangle!")
# else:
#     print("A Scalene Triangle!")

"""
Q5: Classify character type
"""
# Solution:
# ch = input("Enter a single character: ")
# if ord(ch) in range(65, 91):
#     print(f"{ch} is an Uppercase Character")
# elif ord(ch) in range(97, 123):
#     print(f"{ch} is a Lowercase Character")
# elif ord(ch) in range(48, 58):
#     print(f"{ch} is a digit")
# else:
#     print(f"{ch} is a special character")

"""
Q6: Calculate electricity bill
"""
# Solution:
# units = int(input("Enter units: "))
# bill = 0
# if units < 0:
#     print("Invalid units!")
# elif units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = units * 7
# else:
#     bill = units * 10
# print(f"Your bill: {bill}")

"""
Q7: Find the greatest of four numbers (nested if)
"""
# Solution:
# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
# num3 = int(input("num3: "))
# num4 = int(input("num4: "))
# if num1 > num2:
#     if num1 > num3:
#         if num1 > num4:
#             print(f"{num1} is greatest")
#         else:
#             print(f"{num4} is greatest")
#     else:
#         if num3 > num4:
#             print(f"{num3} is greatest")
#         else:
#             print(f"{num4} is greatest")
# else:
#     if num2 > num3:
#         if num2 > num4:
#             print(f"{num2} is greatest")
#         else:
#             print(f"{num4} is greatest")
#     else:
#         if num3 > num4:
#             print(f"{num3} is greatest")
#         else:
#             print(f"{num4} is greatest")

"""
Q8: Check if year is both century and leap year
"""
# Solution:
# year = int(input("Enter any year: "))
# if year % 400 == 0:
#     print(f"{year} is both century and leap year")
# else:
#     print("Not a leap and century year")

"""
Q9: Classify BMI (Body Mass Index)
"""
# Solution:
# bmi = float(input("Enter BMI: "))
# if 0 < bmi < 18.5:
#     print("Underweight")
# elif 18.5 <= bmi <= 24.9:
#     print("Normal")
# elif 25 <= bmi <= 29.9:
#     print("Overweight")
# elif bmi >= 30:
#     print("Obese")
# else:
#     print("Invalid BMI!")

"""
Q10: Find the smallest of three numbers
"""
# Solution:
# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
# num3 = int(input("num3: "))
# if num1 < num2:
#     if num1 < num3:
#         print(f"{num1} is smallest")
#     else:
#         print(f"{num3} is smallest")
# else:
#     if num2 < num3:
#         print(f"{num2} is smallest")
#     else:
#         print(f"{num3} is smallest")


# SECTION 3: FOR LOOP PROBLEMS

"""
Q1: Find Armstrong Numbers (3-digit numbers where sum of cubes = number)
"""
# Solution:
# armstrong_list = []
# for i in range(100, 1000):
#     digit_sum = 0
#     num = i
#     while num > 0:
#         digit = num % 10
#         digit_sum += digit ** 3
#         num = num // 10
#     if digit_sum == i:
#         armstrong_list.append(i)
# print(armstrong_list)

"""
Q2: Print first n prime numbers
"""
# Solution:
# n = int(input("Enter n: "))
# primes = []
# print("Printing n prime numbers in a list: \n")
# num = 2
# while len(primes) != n:
#     is_prime = True
#     for p in primes:
#         if num % p == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(num)
#     num += 1
# print(primes)

"""
Q3: Find numbers divisible by 3 with digit sum <= 10
"""
# Solution:
# result = []
# for i in range(1, 501):
#     if i % 3 == 0:
#         digit_sum = 0
#         num = i
#         while num > 0:
#             digit = num % 10
#             digit_sum += digit
#             num = num / 10
#         if digit_sum <= 10:
#             result.append(i)
# print(result)

"""
Q4: Print diamond pattern with asterisks
"""
# Solution:
# n = int(input("n: "))
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (i + 1) + "*" * i)

"""
Q5: Check if string is pangram
"""
# Solution:
# sentence = input("Enter a string: ").lower()
# unique_letters = []
# for char in sentence:
#     if 97 <= ord(char) <= 122:
#         unique_letters.append(char)
# unique_letters = set(unique_letters)
# if len(unique_letters) == 26:
#     print("It is a pangram")
# else:
#     print("It is not a pangram")

"""
Q6: Find twin primes (primes with difference of 2)
"""
# Solution:
# primes = []
# for i in range(2, 101):
#     is_prime = True
#     for p in primes:
#         if i % p == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(i)
# 
# for i in range(1, len(primes)):
#     if primes[i] - primes[i - 1] == 2:
#         print(f"({primes[i-1]},{primes[i]})")

"""
Q7: Check if number is Harshad Number (divisible by sum of digits)
"""
# Solution:
# num = int(input("Enter a number: "))
# digit_sum = 0
# for digit_char in str(num):
#     digit_sum += int(digit_char)
# if num % digit_sum == 0:
#     print("It is a Harshad Number!")
# else:
#     print("It is not a Harshad Number!")

"""
Q8: Print Pascal's Triangle
"""
# Solution:
# rows = int(input("Enter number of rows: "))
# for row in range(1, rows + 1):
#     value = 1
#     print(" " * (rows - row), end="")
#     for col in range(1, row + 1):
#         print(value, end=" ")
#         value = value * (row - col) // col
#     print()

"""
Q9: Calculate sum of squares from 1 to n
"""
# Solution:
# n = int(input("n: "))
# total = 0
# for i in range(1, n + 1):
#     total += i ** 2
# print("Sum of the series: ", total)

"""
Q10: Check if number is Strong Number (sum of factorials of digits = number)
"""
# Solution:
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
# 
# n = int(input("Enter a number: "))
# digit_string = str(n)
# fact_sum = 0
# temp = n
# for i in range(len(digit_string)):
#     digit = temp % 10
#     fact_sum += factorial(digit)
#     temp = int(temp / 10)
# if n == fact_sum:
#     print("It is a Strong number!")
# else:
#     print("It is not a Strong number")


# SECTION 4: WHILE LOOP PROBLEMS

"""
Q11: Check if reverse of a number is prime
"""
# Solution:
# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# 
# n = int(input("Enter n: "))
# reversed_num = 0
# temp = n
# while temp > 0:
#     digit = temp % 10
#     reversed_num = reversed_num * 10 + digit
#     temp = int(temp / 10)
# 
# if is_prime(reversed_num):
#     print(f"{reversed_num} is prime!")
# else:
#     print(f"{reversed_num} is not prime!")

"""
Q12: Sum of digits until sum exceeds 100
"""
# Solution:
# total_sum = 0
# while total_sum <= 100:
#     n = int(input("Enter a number: "))
#     while n > 0:
#         digit = n % 10
#         total_sum += digit
#         n = int(n / 10)

"""
Q13: Check if number is Duck Number (contains zero but not leading zero)
"""
# Solution:
# def has_zero(num):
#     while num > 0:
#         digit = num % 10
#         if digit == 0:
#             return True
#         num = int(num / 10)
#     return False
# 
# num_str = input("Enter a number: ")
# if not num_str.isdigit():
#     print("Please enter a valid positive integer!")
#     exit(1)
# num = int(num_str)
# if has_zero(num) and num_str[0] != '0':
#     print("It is a Duck number")
# else:
#     print("It is not a Duck number")

"""
Q14: Check if number is Happy Number
"""
# Solution:
# def sum_of_digit_squares(n):
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total += digit ** 2
#         n = n // 10
#     return total
# 
# num = int(input("Enter a number: "))
# seen = set()
# while True:
#     num = sum_of_digit_squares(num)
#     if num == 1:
#         print("It is a happy number!")
#         break
#     elif num in seen:
#         print("It is not a happy number!")
#         break
#     seen.add(num)

"""
Q15: Find the largest prime factor of a number
"""
# Solution:
# num = int(input("Enter a number: "))
# largest_factor = -1
# temp = num
# while temp % 2 == 0:
#     largest_factor = 2
#     temp = temp // 2
# for i in range(3, int(temp ** 0.5) + 1, 2):
#     while temp % i == 0:
#         largest_factor = i
#         temp = temp // i
# if temp > 2:
#     largest_factor = temp
# print(f"{largest_factor} is the largest prime factor of {num}")

"""
Q16: Keep asking for input until palindrome is entered
"""
# Solution:
# while True:
#     input_str = input("Enter a palindrome: ")
#     if input_str == input_str[::-1]:
#         break

"""
Q17: Find digital root (keep summing digits until single digit)
"""
# Solution:
# num = int(input("Enter a number: "))
# while True:
#     digit_sum = 0
#     while num > 0:
#         digit = num % 10
#         digit_sum += digit
#         num = num // 10
#     if 0 <= digit_sum <= 9:
#         print("Single digit number: ", digit_sum)
#         break
#     num = digit_sum

"""
Q18: Generate Collatz sequence
"""
# Solution:
# num = int(input("Enter a number: "))
# print("Collatz sequence: ")
# sequence = []
# while num != 1:
#     if num % 2 != 0:
#         num = 3 * num + 1
#     else:
#         num = num // 2
#     sequence.append(num)
# print(sequence)

"""
Q19: Check if number is Kaprekar Number
"""
# Solution:
# num = int(input("num: "))
# square = num ** 2
# reversed_num = 0
# position = 0
# while square > 0:
#     digit = square % 10
#     reversed_num += digit * (10 ** position)
#     position += 1
#     square = square // 10
#     if square + reversed_num == num:
#         print(f"{square} + {reversed_num} = {num}")
#         break
# else:
#     print("Not a Kaprekar's Number!")

"""
Q20: Simple ATM Simulation
"""
# Solution:
# balance = 0
# while True:
#     print("""
#     Welcome to ATM!
#     1. Check Balance
#     2. Deposit Money
#     3. Withdraw Money
#     4. Exit
#     """)
#     choice = int(input("Enter your choice: "))
#     if choice <= 0 or choice > 4:
#         print("Invalid choice! Enter valid one")
#     elif choice == 1:
#         print(f"Balance: {balance}")
#     elif choice == 2:
#         deposit = int(input("Enter money to be deposited: "))
#         balance += deposit
#     elif choice == 3:
#         withdraw = int(input("Enter money to be withdrawn: "))
#         if balance - withdraw < 0:
#             print("Insufficient Balance!")
#         else:
#             balance -= withdraw
#             print("Balance Deducted!")
#     elif choice == 4:
#         print("Thank you for using ATM!")
#         break