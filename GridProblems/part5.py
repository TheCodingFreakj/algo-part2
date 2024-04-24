def uniquePaths(obstacleGrid):
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    # dp to store the unque paths
    dp = [[0] * cols for _ in range(rows)]


       # Initialize the first row and first column
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    
    # Initialize the first column
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
    
    # Initialize the first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0

    # traverse the rows
    for row in range(1,rows):
        # traver each colm in the row
        for cell in range(1,cols):
            #summit up all the unque path upto dp[row][col]
            if(obstacleGrid[row][cell] != 1):
                if_moves_down = dp[row-1][cell]
                if_moves_right = dp[row] [cell-1]
                dp[row][cell] = if_moves_down + if_moves_right
             

    return dp[rows -1][cols -1]
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePaths(obstacleGrid))
