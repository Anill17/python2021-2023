from collections import deque
def maze():
    m = [[1,1,1,1,1],
         [0,1,1,1,1],
         [0,0,0,0,1],
         [1,0,0,0,0],
         [0,0,0,1,1]]
    
    move_x = [1,0,0,-1]
    move_y = [0,-1,1,0]
    visited = [False for _ in range(len(m)) for _ in range(len(m))]
    min_distance = 0
def is_valid(row,col):
    global m
    global visited
    if row < 0 or row >= len(m):
        return False
    if col < 0 or col >= len(m):
        return False
    if m[row][col] == 1:
        return False
    if visited[row][col]:
        return False
    return True

def search(i,j,destination_x,destination_y):
    global visited
    global move_x
    global move_y
    visited[i][j] = True    
    queue = deque()
    queue.append(i,j,0)

    while queue:
        (i,j,dist) = queue.popleft()

        if i == destination_x and j == destination_y:
            min_distance = dist
            break

        for move in range(len(move_x)):

            next_x = i + move_x[move]
            next_y = j + move_y[move]
            if is_valid(next_x,next_y):
                visited[next_x][next_y] = True
                queue.append(next_x,next_y,dist+1)

def show_results():
    global min_distance
    if min_distance != 0:
        print("the shortest path from source to destination is {}".format(min_distance))

    else:
        print("there is no feasible solution")

