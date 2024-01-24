matrix = [[0,1,1,1],
          [1,0,1,0],
          [1,1,0,1],
          [1,0,1,0]]
num_colors = 3 # number of colors to solve the question if the value is not enough to solve the problem it will return there is no feasible solution
n = len(matrix)
colors = [0 for i in range(n)]

def coloring_problem():
    if solve(0):
        print(colors)
    else:
        print("there is no feasible solution")


def solve(node_index):
    global colors
    if node_index == n:
        return True
    
    for color_index in range(1,n+1):
        if is_color_valid(node_index,color_index):
            colors[node_index] = color_index

            if solve(node_index + 1):
                return True


    return False

def is_color_valid(node_index,color_index):
    for i in range(n):
        if matrix[node_index][i] == 1 and color_index == colors[i]: #
            return False
    return True

coloring_problem()





