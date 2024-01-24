cube = 0.125
epsilon = 0.01
low = 0
high = cube
guess = (high + low)/2.0
if cube < 0:
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 > cube :
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0

elif 0 < cube < 1:
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube :
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0

else:
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube :
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0

print(guess, 'is close to the cube root of', cube)