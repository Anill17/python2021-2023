#Given an integer array nums, return true 
# #if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
# #If no such indices exists, return false.

inp = list(input("please enter a list of numbers: ", ))


for i in range(len(inp)):
    for j in range(len(inp)):
        for k in range(len(inp)):
            if int(inp[i]) < int(inp[j]) < int(inp[k]) == True and j-i == 1 and k - j == 1 and k - i == 2:
                print("True")
            else:
                print("False")

#not complated
