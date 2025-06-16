### functions
# # no params no returns 
# def print_hi():
#     print("Hi")

# # call function
# print_hi()

# # 1 input param no returns 
# def print_backwards(string):
#     print(string[::-1])

# print_backwards("good")

# # 2 input params 1 return
# def calculate_area(l, w):
#     return l*w

# width, length = 5, 3
# the_area = calculate_area(length, width)
# print(the_area)

# # multiple inputs and multiple outputs
# def min_max(nums):
#     return min(nums), max(nums)

# low, high = min_max([1, 2, 3, 4, 5, 6])

# print("low:", low, "\nhigh:", high)


# ### import functions from scripts
# from in_class_2 import print_hi  # import one function
# from in_class_2 import *  # import all functions


# ### import modules (books) from libraries, recommended to be put all in the top
# import matplotlib.pyplot as plt  # plotting library
# import numpy as np  # only for numbers and nested numbers, runs fasters than basic python
import pandas as pd  # for dictionary, use numpy automatically, handles strings and numbers

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# plt.plot(x, y)
# plt.title("my first plot")
# plt.savefig("lession02class")
# plt.show()

# my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(np.mean(my_array))

my_data = {
    "names": ["alice", "marvin"],
    "age": [20, 42]
}

print(my_data)

my_df = pd.DataFrame(my_data)
print(my_df)

### take notes of all the versions of the library in case some codes don't work in the future
