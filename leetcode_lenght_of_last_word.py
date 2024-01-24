def lengthOfLastWord(s):
    s = s.strip()
    spaces = list()
    for i in range(len(s)):
        if s[i] == " ":
            spaces.append(i)
    print(spaces)
    ans = len(s[spaces[-1]:])
    return ans-1

print(lengthOfLastWord("luffy is still joyboy"))