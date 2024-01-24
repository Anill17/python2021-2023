prices = [7,6,4,3,1]
res = list()

best = 0 
for count,i in enumerate(prices):
    for j in range(count,(len(prices))):
        if i < prices[j] and prices[j]-i > best:
            best = prices[j]-i
        

            
        
        
        

print(best)