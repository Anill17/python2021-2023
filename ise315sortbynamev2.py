def listToString(s):
 
    # initialize an empty string
	str1 = ""
 
    # traverse in the string
	for ele in s:
		str1 += ele
		str1 += " "
 
    # return string
	return str1

def partition(array, low, high):

	# Choose the rightmost element as pivot
	pivot = array[high]

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:
			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# e greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# Function to perform quicksort


def quick_sort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quick_sort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quick_sort(array, pi + 1, high)


def partition_profit(array, low, high):

	# Choose the rightmost element as pivot
    # [-1] used for selecting the last element in list whick is profit
	pivot = int(float(array[high][-1]))

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if int(float(array[j][-1])) <= pivot:
			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# e greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# Function to perform quicksort


def quick_sort_profit(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition_profit(array, low, high)

		# Recursive call on the left of pivot
		quick_sort_profit(array, low, pi - 1)

		# Recursive call on the right of pivot
		quick_sort_profit(array, pi + 1, high)


dict1 = dict()
n = int(input("please enter the column number: ",))
def sortbyname():
    list1 = list()
    with open ("sales.txt", "r") as fp:
        for i in range(n):
            line = fp.readline()
            read = line.split()
            if read != ["Country", "Item", "Type", "Order", "ID", "Units", "Sold", "Total", "Profit"]:
                list1.append(read)
            quick_sort(list1, 0, len(list1)-1)

    with open("sortedbyname.txt","w") as fp:
        for i in range(len(list1)):
            element = " ".join(list1[i])
            fp.writelines(element)
            fp.writelines("\n")
    
sortbyname()

def sortbyname_profit():
	list2 = list()
	with open ("sortedbyname.txt","r") as fp:
		for i in range(n):
			line = fp.readline()
			read = line.split()
			if read != ["Country", "Item", "Type", "Order", "ID", "Units", "Sold", "Total", "Profit"]:
				dict1[i] = read
		
		flag = dict1[0][0]
		list2.append(dict1[0])
        #ülke isimleri için 2. indeksede bakılmalı 
		for i in range(1,len(dict1)-1):
			 
			if dict1[i][0] == flag:
				list2.append(dict1[i])
				flag = dict1[i][0]   
            	
			else:
				with open("sortedbyname2.txt","a") as fp:
					quick_sort_profit(list2, 0, len(list2)-1)
					for k in range(len(list2)):
						item = (list2[k])
						str1 = listToString(item)
						fp.writelines(str1)
						fp.writelines("\n")
				list2.clear()
				flag = dict1[i][0]

sortbyname_profit()


