# def cutRod(prices, n):
# 	mat = [[0 for i in range(n+1)]for j in range(n+1)]
# 	for i in range(1, n+1):
# 		for j in range(1, n+1):
# 			if i == 1:
# 				mat[i][j] = j*prices[i-1] 
# 			else:
# 				if i > j:
# 					mat[i][j] = mat[i-1][j]
# 				else:
# 					mat[i][j] = max(prices[i-1]+mat[i][j-i], mat[i-1][j])
# 	return mat[n][n]


# prices = [1, 5, 8, 9, 10, 17, 17, 20]
# # n = len(prices)

# print("Maximum obtained value is ", cutRod(prices, n))

# This Code is Contributed By Vivek Maddeshiya

mat=[1,2,3,4]
print(mat[1][0])