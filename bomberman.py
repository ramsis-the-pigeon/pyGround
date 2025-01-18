import random
import time


r, c, n = map(int, input("Enter three integers separated by spaces: ").split())



def createGrid(rows, columns):
    return[["." for _ in range(columns)] for _ in range(rows)]
 
bomb_positions = set()
def addBombs(grid):
    rows = len(grid)
    columns = len(grid[0])
    num_bombs = random.randint(1, (rows * columns) // 2)
    
    while len(bomb_positions) < num_bombs:
        row = random.randint(0, rows - 1)
        col = random.randint(0, columns - 1)
        bomb_positions.add((row, col))
    
    for row, col in bomb_positions:
        grid[row][col] = "o"
    
    return grid, bomb_positions

############################# step 1: create the grid, add bombs
grid = createGrid(r, c)
grid_with_bombs = addBombs(grid)[0]


for row in grid_with_bombs:
    print(" ".join(row))



############################# step 2: Bomberman plants bombs in all cells without bombs
time.sleep(1)

def fillWithBombs():
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid_with_bombs[i][j] == 'o':
                pass
            else: 
                grid_with_bombs[i][j] = 'o'
    print()
    for row in grid_with_bombs:
        print(" ".join(row))
fillWithBombs()



################ step 3: After one more second, any bombs planted exactly three seconds ago will detonate
time.sleep(1)

def detonate():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in bomb_positions: 

                grid_with_bombs[i][j] = '.'

                # List of neighbors
                neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

                for ni, nj in neighbors:
                    # Check if neighbor indices are within bounds
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                        grid_with_bombs[ni][nj] = '.'
            
    

    print()
    for row in grid_with_bombs:
        print(" ".join(row))
detonate()

while True:
    new_bomb_position = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'o':
                new_bomb_position.add((i, j))
    bomb_positions = new_bomb_position
    time.sleep(1)
    fillWithBombs()
    time.sleep(1)
    detonate()