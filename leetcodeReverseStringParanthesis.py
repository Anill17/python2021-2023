class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        while '(' in s:
            indeks = 0
            for i in range(len(s)):
                if s[i] == '(':
                    indeks = i
                elif s[i] == ')':
                    s = s.replace(s[indeks:i+1], s[indeks+1:i][::-1])
                    break
        return s