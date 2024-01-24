def digitSum(number):
    Sum = 0
    while number != 0:
        lastDigit = number % 10 # Get the remainder with using "%10"
        Sum += lastDigit
        number = number // 10 # Get rid of the remainder with using "//10"
    return Sum
print("Test...")
print("Input:",5631298,"\nOutput:", digitSum(5631298))

def ddigitSum(number):
    Sum = 0
    while number != 0:
        lastDigit = number % 10 # Get the remainder with using "%10"
        Sum += lastDigit
        number = number // 10 # Get rid of the remainder with using "//10"
        
    if Sum // 10 > 0: # Checkpoint before recursive call
        return digitSum(Sum) # Recursive call
    else:
        return Sum
print("Test...")
print("Input:", 56312989, "\nOutput:",ddigitSum(5631298))