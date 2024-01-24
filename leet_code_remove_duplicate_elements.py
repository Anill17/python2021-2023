nums = [0,0,1,1,1,2,2,3,3,4]
# # 5, nums = [0,1,2,3,4,_,_,_,_,_]
# dict1 = dict()
# ct = 0 
# for i in nums:
#     if i not in dict1:
#         dict1[i] = 1 
#     else:
#         dict1[i] += 1 


# try:
#     for i in dict1:
#         while dict1[i] != 1:
#             nums.remove(i)
#             ct += 1

#     for i in range(ct):
#         nums.append("_")

# except:
#     ValueError  


# print(nums)

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            nums[j] = "_"

for j in range(len(nums)):
    for i in range(len(nums)-1):
        if nums[i] == "_":
            nums[i], nums[i+1] = nums[i+1],nums[i]
print(nums)


    