nums = [2,7,11,15]
target = 22

for i in range(len(nums)):
    for j in range(len(nums)):
        temp = nums[i] + nums[j]
        if temp == target:
            print(i,j)
            break
          