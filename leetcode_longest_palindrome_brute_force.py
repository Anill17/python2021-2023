def find_longest_palindrome(s):
    longest = ''
    n = len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            word = s[i:j]
            if word == word[::-1]:
                if len(word)>len(longest):
                    longest = word          
    return longest


print(find_longest_palindrome('locoannamadam'))
# madam

print(find_longest_palindrome('anna'))
# anna

print(find_longest_palindrome('abc'))
# a