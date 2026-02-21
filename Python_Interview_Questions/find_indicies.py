"""
Problem: Find the indices of two numbers in the list whose sum equals the target value.

Approach:
Use a dictionary to store previously visited numbers and their indices.
For each number, calculate (target - current number) and check if it already exists.
If it exists, we found the pair whose sum equals the target.

Time Complexity:-   O(n)
Space Complexity:-  O(n)

"""

#######
# nums = [2, 7, 11, 15]
# target = 9

# data = {}

# for i, num in enumerate(nums):
#     diff = target - num
#     if diff in data:
#         print(data[diff], i)
#     data[num] = i
########


def find_indecies_of_two_sum(nums, target):
    data = {}

    for i, num in enumerate(nums):
        diff = target - num
        
        if diff in data:
            return [data[diff], i]

        data[num] = i

nums = [2, 7, 11, 15]
target = 9
print(find_indecies_of_two_sum(nums, target))




"""
nums = [2, 7, 11, 15]
target = 9

# Create a dictionary to store numbers that we have already visited
# Key   -> number from the list
# Value -> index of that number in the list
data = {}

# enumerate() is used to get both the index (i) and the value (num) while iterating
for i, num in enumerate(nums):

    # Calculate the number required to reach the target
    # Example: if num = 2 and target = 9, then we need 7 (9 - 2)
    diff = target - num

    # Check if the required number (diff) already exists in the dictionary
    # If it exists, it means we have already seen that number earlier
    # and together with the current number it will make the target sum
    if diff in data:

        # Print the index of the previously seen number (stored in dictionary)
        # and the index of the current number
        # These two indices correspond to numbers whose sum equals the target
        print(data[diff], i)

    # Store the current number and its index in the dictionary
    # This allows future iterations to check if they need this number
    data[num] = i
"""