MOD = 10**9 + 7

def isSafe(x, y, grid, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '.' and not visited[x][y]

def countPaths(x, y, grid, visited):
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        return 1
    
    if not isSafe(x, y, grid, visited):
        return 0
    
    visited[x][y] = True
    
    paths = (countPaths(x + 1, y, grid, visited) + countPaths(x, y + 1, grid, visited)) % MOD
    
    visited[x][y] = False
    return paths

def findPaths(grid):
    
    visited = [[False] * len(grid) for _ in range(len(grid))]
    
    return countPaths(0, 0, grid, visited)


file1 = open("grid_paths_test_file1.txt", "r")
f = file1.read()
file1.close()
print(f)

n = int(input())  
grid = [list(input()) for _ in range(n)]
ans = findPaths(grid)%MOD

file1 = open("output.txt", "a")  # append mode
file1.write(ans)
file1.close()

