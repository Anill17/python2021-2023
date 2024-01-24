import math

def height(a):
  return a*math.sqrt(3)/2

notriangle = -1
total_height = 0
init_a = 1
a      = init_a

hght = height(init_a)

while hght > 0.000001*init_a:
  
  notriangle = notriangle +2
  total_height += hght
  print(notriangle, total_height, hght)
  a = a/4
  hght = height(a)
  
print(notriangle,total_height, total_height*init_a)

notriangle = 1
 
init_a = 1
a      = init_a

total_height = height(init_a)

while  total_height*init_a < (2/math.sqrt(3)-0.00000001)*init_a*init_a:
  notriangle = notriangle +2
  a = a/4
  hght = height(a)
  total_height += hght
  #print(notriangle, total_height, hght, total_height*init_a)

print(notriangle,total_height, total_height*init_a)
  
################################################################

import math
tiles=[[0,0],
       [0,1],[1,1],
       [0,2],[1,2],[2,2],
       [0,3],[1,3],[2,3],[3,3],
       [0,4],[1,4],[2,4],[3,4],[4,4],
       [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],
       [0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],
       [0,7],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],
       [0,8],[1,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8],[8,8],
       [0,9],[1,9],[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],[9,9]]

sum_tiles = []
val1_tiles = []
val2_tiles = []

for i in tiles:
  sum_tiles.append(i[0]+i[1])
  val1_tiles.append(i[0]*10+i[1]) 
  val2_tiles.append(i[0]+i[1]*10) 
print (sum_tiles)
#"""
for i in range(10):
  for j in range(10):
    if i!=j:
      for k in range(10):
        if i!=k and k!=j:
          for m in range(10):
            if m!=i and m!=j and m!=k:
              total = sum_tiles[i]+sum_tiles[j]*10+sum_tiles[k]*100+sum_tiles[m]*1000
              if total > 9999 :
                break
              else:
                tile1_val1 = int(total/100)
                tile0_val1 = int(total%100)
                if tile1_val1 != tile0_val1:
                  tile1_val2 = int(tile1_val1//10+(tile1_val1%10)*10)
                  tile0_val2 = int(tile0_val1//10+(tile0_val1%10)*10)
                  if tile1_val1 != tile0_val2:
                    tile1 = [int(tile1_val1//10), int(tile1_val1%10)] 
                    tile0 = [int(tile0_val1//10), int(tile0_val1%10)]
                    ind1 = tiles.index(tile1)
                    ind0 = tiles.index(tile0)
                    if ind1 != i and ind1 != j  and ind1 !=k and ind1  !=m and ind0 != i and ind0 != j  and ind0 !=k and ind0  !=m:
                      print (i, j, k, m, ind1, ind0)
"""                    
                    tile1r = [tile1[1],tile1[0]]
                    tile0r = [tile0[1],tile0[0]]

"""



print(40*"=")  
#================================================


import math
tiles=[[0,0],
       [0,1],[1,1],
       [0,2],[1,2],[2,2],
       [0,3],[1,3],[2,3],[3,3],
       [0,4],[1,4],[2,4],[3,4],[4,4],
       [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],
       [0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],
       [0,7],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],
       [0,8],[1,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8],[8,8],
       [0,9],[1,9],[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],[9,9]]

def tile_index_list(n1,n2,n):
  tilelist =[]
  ns = n1 + n2
  p_10=int(math.pow(10,n))
  for i in range (n):
    p_10=p_10//10
    tilelist.append([n1//p_10,n2//p_10])
    if (n1//p_10) != (n2//p_10):
      tilelist.append([n2//p_10,n1//p_10])
    n1  = n1 - (n1//p_10)*p_10
    n2  = n2 - (n2//p_10)*p_10
    
  p_10=int(math.pow(10,n+1))
  
  for i in range (n//2):
    p_10=p_10//100

    tilelist.append([ns//p_10, (ns-(ns//p_10)*p_10)//(p_10//10)])
    if (ns//p_10) != ((ns-(ns//p_10)*p_10)//(p_10//10)):
      tilelist.append([(ns-(ns//p_10)*p_10)//(p_10//10), ns//p_10 ])
    ns  = ns - (ns//(p_10//10))*(p_10//10)


  #print(tilelist)

  t_index=[]
  for i in range (len(tilelist)):
    if tilelist[i] in tiles:
      t_index.append(tiles.index(tilelist[i]))

  #print(t_index)

  for i in range (len(t_index)):
    if t_index[i] in t_index[i+1:]:
      return False
  
  return True
    
count=0
for i in range (0,9999):
  print("....",i)
  for j in range (0,9999):
    if i+j < 10000:
      if tile_index_list(i,j,4):
        #print (i," + ",j," = ",i+j)
        count +=1
 
print(count, 1000000-count)

################################################################

import random
import math

orange = 0
blue = 0
green = 0
red = 0

def insquare(rx,ry,l,x,y):
  if rx <= x + l/2 and rx > x - l/2 and  ry <= y + l/2 and ry > y - l/2:
    return True
  return False

def incircle(rx,ry,x,y,r):
  if ((rx-x)*(rx-x)+(ry-y)*(ry-y)) <= (r * r):
    #print("True",x,y)
    return True
  #print("False",x,y,(rx-x)*(rx-x)+(ry-y)*(ry-y))
  return False

for i in range (1000000):
  x = random.random()*10-5
  y = random.random()*10-5
  #x = float(input())
  #y = float(input())
  if incircle(x,y,3,3,2) or incircle(x,y,3,-3,2) or incircle(x,y,-3,-3,2) or incircle(x,y,-3,3,2):
    orange += 1
    #print("orange",orange, x,y)
  elif insquare(x,y,6,0,0):
    blue += 1
    #print("blue",blue, x,y)
  elif incircle(x,y,0,0,5):
    green += 1
    #print("green",green, x,y)
  else:
    red += 1
    #print("red",red, x,y)

print(orange, blue, green, red)

print(orange*(9-math.pi), blue*4*math.pi)
################################################################

array2sort=[8,15,6,13,2,7,12,5,9,4,10]
keyindex =7


def recsearch(arr,ki):
  print(ki,arr)
  pivot = arr[0]
  smaller = []
  greater = []
  for i in range(1,len(arr)):
    if arr[i] < pivot :
      smaller.append(arr[i])
    else:
      greater.append(arr[i])
  
  if len(smaller) == ki -1:
    return pivot
  elif  len(smaller) >= ki:
    pivot=recsearch(smaller,ki)
  else:
    pivot=recsearch(greater,ki-len(smaller)-1)
  return pivot
print(recsearch(array2sort,keyindex))

################################################################
import math
tiles=[[0,0],
       [0,1],[1,1],
       [0,2],[1,2],[2,2],
       [0,3],[1,3],[2,3],[3,3],
       [0,4],[1,4],[2,4],[3,4],[4,4],
       [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],
       [0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],
       [0,7],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],
       [0,8],[1,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8],[8,8],
       [0,9],[1,9],[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],[9,9]]

def tile_index_list(n1,n2,n):
  tilelist =[]
  ns = n1 + n2
  p_10=int(math.pow(10,n))
  for i in range (n):
    p_10=p_10//10
    tilelist.append([n1//p_10,n2//p_10])
    if (n1//p_10) != (n2//p_10):
      tilelist.append([n2//p_10,n1//p_10])
    n1  = n1 - (n1//p_10)*p_10
    n2  = n2 - (n2//p_10)*p_10
    
  p_10=int(math.pow(10,n+1))
  
  for i in range (n//2):
    p_10=p_10//100

    tilelist.append([ns//p_10, (ns-(ns//p_10)*p_10)//(p_10//10)])
    if (ns//p_10) != ((ns-(ns//p_10)*p_10)//(p_10//10)):
      tilelist.append([(ns-(ns//p_10)*p_10)//(p_10//10), ns//p_10 ])
    ns  = ns - (ns//(p_10//10))*(p_10//10)


  #print(tilelist)

  t_index=[]
  for i in range (len(tilelist)):
    if tilelist[i] in tiles:
      t_index.append(tiles.index(tilelist[i]))

  #print(t_index)

  for i in range (len(t_index)):
    if t_index[i] in t_index[i+1:]:
      return False
  
  return True
    
count=0
for i in range (0,9999):
  print("....",i)
  for j in range (0,9999):
    if i+j < 10000:
      if tile_index_list(i,j,4):
        #print (i," + ",j," = ",i+j)
        count +=1
 
print(count, 1000000-count)
################################
def check (list2, wallet):
    c_50 = list2.count(50)
    if c_50 < wallet[4][1]:
        c_20 = list2.count(20)
        if c_20 < wallet[3][1]:
            c_10 = list2.count(10)
            if c_10 < wallet[2][1]:
                c_5 = list2.count(5)
                if c_5 < wallet[1][1]:
                    c_1 = list2.count(1)
                    if c_1 < wallet[0][1]:
                        print(list2)

wallet = [ (1,7), (5,3), (10,1), (20,4), (50,3)]

money = int(input("Input: "))

a_50 = money//50
money -= 50*a_50
a_20 = money//20
money -= 20*a_20
a_10 = money//10
money -= 10*a_10
a_5 = money//5
money -= 5*a_5
a_1 = money//1

list2 = []

for i in range(0,a_50):
    list2.append(50)
for i in range(0,a_20):
    list2.append(20)
for i in range(0,a_10):
    list2.append(10)
for i in range(0,a_5):
    list2.append(5)
for i in range(0,a_1):
    list2.append(1)
check(list2, wallet)
while len(list2) != money:
    while list2.count(50)>0:
        list2.remove(50)
        list2.append(10)
        list2.append(20)
        list2.append(20)
        check(list2, wallet)
    while list2.count(20)>0:
        list2.remove(20)
        list2.append(10)
        list2.append(10)
        check(list2, wallet)
    
    while list2.count(10)>0:
        list2.remove(10)
        list2.append(5)
        list2.append(5)
        check(list2, wallet)
    
    while list2.count(5)>0:
        list2.remove(5)
        for i in range(5):
            list2.append(1)
        check(list2, wallet)