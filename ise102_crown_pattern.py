def crown(n):
  for i in range (1,n+1):
    
    for j in range (1,i+1):
      print(i, end="" )
    for j in range (1,2*(n-i)+1):
      print(" ", end="" )
    for j in range (1,2*i):
      print(i, end="" )
    for j in range (1,2*(n-i)+1):
      print(" ", end="" )
    for j in range (1,i+1):
      print(i, end="" )
    print("")

crown(5)