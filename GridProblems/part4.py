def uniquePaths(rows, cols):
    # dp to store the unque paths
    dp = [[0] * cols for _ in range(rows)]


    # Initialize the number of unique paths for the first row and first column to 1
    for i in range(rows):
        dp[i][0] = 1
    for j in range(cols):
        dp[0][j] = 1

    # traverse the rows
    for row in range(1,rows):
        # traver each colm in the row
        for cell in range(1,cols):
            #summit up all the unque path upto dp[row][col]
            if_moves_down = dp[row-1][cell]
            if_moves_right = dp[row] [cell-1]
            dp[row][cell] = if_moves_down + if_moves_right
            # print(dp[row][cell])

    return dp[rows -1][cols -1]
m = 3
n = 7
print(uniquePaths(m, n))
