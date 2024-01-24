def letterCombinations(digits):

    res = list()
    digitToChar = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jk]",
                    "6":"mno",
                    "7":"aprs",
                    "g":"tuv"}
    
    def backtrack(i, curStr):
        if len(curStr) == len(digits) :
            res.append (curStr)
            return
        for c in digitToChar[digits[i]]:
            backtrack(i + 1, curStr + c)
    backtrack(0,"")

    print(res)

letterCombinations("23")