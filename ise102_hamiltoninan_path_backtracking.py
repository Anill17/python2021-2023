matrix = [[0,1,0,0,0,1],
          [1,0,1,0,0,0],
          [0,1,0,0,1,0],
          [0,0,0,0,1,1],
          [0,0,1,1,0,1],
          [1,0,0,1,1,0]]
            
n = len(matrix)   

def hamiltonian_path(path):
    global matrix
    global n
    if solve(1,path):
        show_hamitonian_path(path)
    else:
        print("there is no feasible solution", )

def solve(position,path):
    global n
    global matrix 
    if position == n:
        return True
    
    for vertex in range(1,n):
        if feasible(vertex,position,path):
            path.append(vertex)
            
            if solve(position+1,path):
                return True

            path.pop() ### backtracking
    return False

def feasible(vertex,position,path):
    if matrix[position-1][vertex] == 0:
        return False
    
    for i in range(position):
        if path[i] == vertex:
                return False
    return True

def show_hamitonian_path(path):
    for i in path:
        print(i)


hamiltonian_path([0])