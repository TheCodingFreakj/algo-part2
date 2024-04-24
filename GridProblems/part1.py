#Minimum Path Sum in a Grid: 
#Given a grid filled with non-negative numbers, 
#find a path from the top-left corner to the bottom-right corner 
#that minimizes the sum of numbers along the path.


def min_path_sum(grid):
    print(grid, len(grid))

    rows = len(grid)
    cols = len(grid[0])
    
    #Initialize a DP table to store minimum path sums
    #Initialize the similar structure as grid
    dp = [[0] * cols for _ in range(rows)]

    #Initialize the first cell
    dp[0][0] = grid[0][0]

    # Fill the first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill the first col
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]  

    print(dp) 

    #we have to fill the rest part

    #iterating on the rows first
    for row in range(rows):
        #iterating on the cols first
        for col in range(cols):
            #getting the minimum path sum to cell dp[row][col]
            #taking the min value from either 
            #previous cell above cell dp[row][col]: dp[i] [j-1]
            #previous cell left to the cell dp[row][col]: dp[i-1][j]
            #adding the current value of grid [row] [col]
            dp[row][col ] = grid[row][col] + min(dp[i-1][j], dp[i][j-1])     


    #returning the bottom right part of the dp array which is the min
    return dp[row-1][col-1]




# Example usage:
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(min_path_sum(grid))  # Output should be 7