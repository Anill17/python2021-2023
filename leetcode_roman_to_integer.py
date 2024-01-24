numbers = {
"I" : 1,
"V" : 5,
"X" : 10,
"L" : 50,
"C" : 100,
"D" : 500,
"M" : 1000
}
def romanToInt(s):
    result = 0
    for a, b in zip(s, s[1:]):
        if numbers[a] < numbers[b]:
            result -= numbers[a]
        else:
            result += numbers[a]
    return result + numbers[s[-1]]

print(romanToInt("MCMXCIV"))