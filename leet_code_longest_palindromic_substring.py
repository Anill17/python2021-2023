def longest_palindrome(s):
    curr_long_palindrome = (0,1)
    for i in range(1,len(s)):
        
        odd_palindrome = expand_around_center(s,i-1,i+1)
        even_palindrome = expand_around_center(s,i-1,i)


        longest_palindrome = max(odd_palindrome,even_palindrome, key=lambda x: x[1]-x[0])
        curr_long_palindrome = max(longest_palindrome,curr_long_palindrome,key =lambda x: x[1]-x[0])
    
    return s[curr_long_palindrome[0]:curr_long_palindrome[1]]


def expand_around_center(s,left,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1 


        return[left+1,right]
    
print(longest_palindrome("tenet"))