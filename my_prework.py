# # Question 1
# # Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.


# def hello_name(user_name):
#     print("Hello_"+user_name)
# name = input("Whats your name ")
# hello_name(name +"!")
# #         .....
# # Question 2
# # Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


# def first_odds():
#     print("")  
# for i in range (1,101):
#     if i % 2 == 1:
#         print(i)
# first_odds()
# # Question 3
# # Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.


# def max_num_in_list(a_list):
#     print()
# list1 = [1,2,3,4,5]
# maxnumber = max(list1)
# print(maxnumber)
# # Question 4
# # Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

# def is_leap_year(a_year):    
#     leap = False
# if (year % 4 == 0) and (year % 100 = 0):
#        leap = True
# elif(year % 100 ==0) and (year % 400 !=0):
#        leap = False
# elif (year % 400 == 0):
#     leap=True
# else:
#      leap = False

# return leap
# # Question 5
# # Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.


#  list = (1,2,2,3)

# def is_consecutive(a_list):
#     if not a_list:
#      return False
# if len(set(a_list)) != len (a_list)