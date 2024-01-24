catogories = ["concert", "theatre", "movie", "museum"]


def biletix():
    dict1 = {"child": 0, "student": 0, "adult": 0}
    price = 0 
    discount = 0 
    while True:
        inp = input("please choose the catogory or type quit to checkout: ", )
        
        if inp == "quit":
            if dict1["child"] >= 5:
                discount += 10
            if dict1["student"] >= 5:
                discount += 5
            if dict1["adult"] >= 5:
                discount += 3
            price -= (price/100) * discount
            return price

            

        if inp in ["concert", "museum"]:
            age = int(input("please enter your age: ", ))
            i = int(input("how many tickets would you like to buy: "))

            if age <= 5:
                price += 7.5*i
                dict1["child"] += 1
            elif age <= 18:
                price += 12.5*i
                dict1["student"] += 1
            elif age <= 59:
                price += 20*i
                dict1["adult"] += 1
            elif age >= 60:
                price += 15*i
        if inp in ["theatre", "movie"]:
            age = int(input("please enter your age: ", ))
            i = int(input("how many tickets would you like to buy: "))

            if age <= 5:
                price += 17.5*i
                dict1["child"] += 1
            elif age <= 18:
                price += 18.5*i
                dict1["student"] += 1
            elif age <= 59:
                price += 27*i
                dict1["adult"] += 1
            elif age >= 60:
                price += 20*i
        else:
            print("unexpected input")
            
            
print(biletix())