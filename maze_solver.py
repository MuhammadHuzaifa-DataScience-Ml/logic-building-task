from collections import deque

# Function to check if a position in the maze is valid
def IsValid(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != '#'

# Function to get valid neighboring positions of a given position in the maze
def get_neighbors(grid, row, col):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
       new_row, new_col = row + dr, col + dc
       if IsValid(grid, new_row, new_col):
           neighbors.append((new_row, new_col))
    return neighbors

# Breadth-first search function to find a path from start to exit in the maze
def bfs(grid, start):
    rows = len(grid)
    columns = len(grid[0])
    visited = set()
    queue = deque([(start, [])])  # Initialize the queue with start position and an empty path
    while queue:
        (row, col), path = queue.popleft()
        if grid[row][col] == 'E':  # If the current position is the exit, return the path
            return path + [(row, col)]
        if (row, col) not in visited:
            visited.add((row, col))
            for neighbor in get_neighbors(grid, row, col):
                queue.append((neighbor, path + [(row, col)]))  # Append neighbor and updated path to the queue
    return None  # If no path found, return None

# Depth-first search function to find a path from start to exit in the maze
def dfs(grid, start):
    rows = len(grid)
    columns = len(grid[0])
    visited = set()
    stack = [(start, [])]  # Initialize the stack with start position and an empty path
    while stack:
        (row, col), path = stack.pop()
        if grid[row][col] == 'E':  # If the current position is the exit, return the path
            return path + [(row, col)]
        if (row, col) not in visited:
            visited.add((row, col))
            for neighbor in get_neighbors(grid, row, col):
                stack.append((neighbor, path + [(row, col)]))  # Append neighbor and updated path to the stack
    return None  # If no path found, return None

# Function to solve the maze using breadth-first search
def solve_maze_with_bfs(maze):
    start = None
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'S':
               start = (row, col)
               break
        if start: 
            break
    if not start: 
        return "Start point not found!"

    path_bfs = bfs(maze, start)  # Find path using BFS

    if path_bfs:
        return path_bfs  # If path found, return the path
    else:
        return "No path found!"  # If no path found, return appropriate message

# Function to solve the maze using depth-first search
def solve_maze_with_dfs(maze):
    start = None
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'S':
               start = (row, col)
               break
        if start: 
            break
    if not start: 
        return "Start point not found!"

    path_dfs = dfs(maze, start)  # Find path using DFS

    if path_dfs:
        return path_dfs  # If path found, return the path
    else:
        return "No path found!"  # If no path found, return appropriate message

# Define the maze
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]

# Solve the maze using BFS and DFS
sol_for_bfs = solve_maze_with_bfs(maze)
sol_for_dfs = solve_maze_with_dfs(maze)

# Print the results
if isinstance(sol_for_bfs, list):
    print("Path found with BFS:")
    for row, col in sol_for_bfs:
        maze[row][col] = '*'  # Mark the path with '*'
    for row in maze:
        print(' '.join(row))  # Print the maze with marked path
else:
    print(sol_for_bfs)  # If no path found with BFS, print appropriate message

if isinstance(sol_for_dfs, list):
    print("\nPath found with DFS:")
    for row, col in sol_for_dfs:
        maze[row][col] = '*'  # Mark the path with '*'
    for row in maze:
        print(' '.join(row))  # Print the maze with marked path
else:
    print(sol_for_dfs)  # If no path found with DFS, print appropriate message
