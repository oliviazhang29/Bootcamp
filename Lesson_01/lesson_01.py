# x = 5  # int
# y = 3.14  # float

# print(type(x)) # get type

# name = "Alice" # string

# # function to add stuff together
# def add_stuff(a, b):
#     result = a + b
#     return result    # return the addition result

# a = 1
# b = 2
# sum = add_stuff(a, b)
# print("the result:", sum, "!")

# # capture input
# usr_num1 = input("Enter number: ")
# usr_num2 = input("Enter another number: ")
# usr_sum_result = add_stuff(int(usr_num1), int(usr_num2))
# print(usr_sum_result)

# # save result to a text file
# with open("result.txt", "w") as file: 
#     file.write(str(usr_sum_result))    # it re-writes the file everytime it runs

# #read from a file
# with open("result.txt", 'r') as file:
#     read_result = int(file.read())
#     print("We read the file:", read_result)

# logic -- if...else... & and/or
# x = 15
# y = -5

# if x > y:
#     print("Yes, x is greater than y!")
#     print("Hi!!!")
# elif y > x:
#     print("Y is greater than x!")
#     print("Yayyyy!")
# elif y == x:
#     print("They are the same!")
# else:
#     print("Failed!")

# if x < 0 and y < 0:
#     print("Yayyyy!")
# elif x < 0 or y < 0:
#     print("Okay... I guess")
# else:
#     print("Boooo....99")

# print("Done!")



# data structure (list, dictionary)
# num_list = [4, 6, 8]
# # print(len(num_list))
# print(num_list[-2])

# my_list = [num_list, "Olivia", "Hailey", "Eden"] # nested list within a list; list can contain strings and numbers at the same time
# print(my_list[0][2])

# my_dict = {     # dictionaries has key values, which allows you to name your variables
#     "numbers": [1, 2, 3], 
#     "names": ["Olivia", "Hailey", "Eden"], 
#     "nested_dict": {"stuff":123, "more_stuff": 567}     # dictionary nested within a dictionary
# }

# print(my_dict["nested_dict"]["stuff"])



# for loop
# max_number = 100

# for i in range(max_number):   # essentially creating a list of [0, 1, 2, 3, 4...99]
#     print(i)

string = "Ashley"

for character in string:
    print(character, end = "")
#    print(character)

# num_list = [4, 6, 8]

# for x in num_list:
#     print(x)