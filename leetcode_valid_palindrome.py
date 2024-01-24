import string
def palindrome(s):
    new_str = ""
    for i in s:
        if i in string.ascii_letters:
            new_str += i
    new_str = new_str.lower()

    for i in range(len(new_str)):
        if new_str[i] == new_str[len(new_str)-1-i]:
            continue
        else:
            return False
    return True

print(palindrome(" man, a plan, a canal: Panama"))