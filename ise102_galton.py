import random

def Galton_Board(trys,numofbuckets):

  move = ['R', 'L']  # 0 = left, 1 = right
 
  buckets = []

  for i in range(numofbuckets):
    buckets.append(0) 
  
  for i in range(trys):     
    sumof = 0
    for j in range(numofbuckets-1):
      x = random.choice(move)
      if x == 'R':
        sumof += 1

    buckets[sumof] +=1
  
  for o in range(numofbuckets):
    print('possibility of getting in to hole ', j+1, ' :', buckets[j] * 100 / trys)
  return

Galton_Board(1000000,7)
