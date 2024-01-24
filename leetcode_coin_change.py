ct = 0 
def coinchange(coins,amount,idx):
    global ct
    if idx < 0 or amount == 0:
        return ct
    elif coins[idx] > amount:
        idx -= 1
        return coinchange(coins,amount,idx)
    else:
        ct += 1
        return coinchange(coins, amount-coins[idx], idx)

print(coinchange([1,2,5],11,2))

