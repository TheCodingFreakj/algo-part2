def min_path_sum(grid, moveCost):
    rows = len(grid)
    cols = len(grid[0])

    # create a 2D array which stores minimum cost of a path that starts from any cell in the first row and ends at any cell in the last row.
    dp = [[0] * cols for _ in range(rows)]

    # #Initialize the first cell of dp as same as grid 
    #because we want to start calc the cost moving from this cells to next row cells
    dp[0] = grid[0]

    

    # we have to calculate the cost of going from ccurrent row to next row any colums

    # iterate the rows first starting from first row and until second last row
    # the goal of loops is to land to a cell in the current row and col
    for row in range(rows-1):
        # iterate over the cells in a particular row
        for cell in range(cols):
            # print(grid[row][cell])
            # from cells on this row we need to move to any cell in the next row
            current_row = row
            current_col = cell
            next_row = current_row + 1

            # now we are reachable to each cell of the grid
            # we will make possible moves from each cells in the current row to the next row
            for next_col in range(cols):
                #calc the new cost by adding min cost stored in dp array 
                #and value in moveCost matrix for the same cell as value and column as stated in question
                cost = dp[current_row][current_col] + \
                    moveCost[grid[current_row][current_col]][next_col]
                #fill the next value based on current value and new cost calulated
                dp[next_row][next_col] = max(
                    cost, dp[current_row][current_col])
                print(dp[next_row][next_col],dp[current_row][current_col])
                

    return dp[next_row][next_col]


# Example usage:
# grid = [[5, 1, 2], [4, 0, 3]]
# moveCost = [[12, 10, 15], [20, 23, 8], [
#     21, 7, 1], [8, 1, 13], [9, 10, 25], [5, 3, 2]]
grid = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
moveCost = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, 24],
    [25, 26, 27]
]
print(min_path_sum(grid, moveCost))
