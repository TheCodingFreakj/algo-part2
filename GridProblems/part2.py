# Minimum Cost Path in a Matrix with Limited Moves:
# Given a matrix with values representing costs,
# and limited moves in each direction,
# find the minimum cost path from the top-left corner to the bottom-right corner.


# define all directions
# add items to the priority queue - cost, current posn in direction, moves taken so far
# created a visited set to track visted positions
# start a loop until the queue is empty
    # inside the loop remove the first item
    # if current position is equal to destination return cost
    # if current position is in visited set then continue else add it to visited set
        # Run an inner loop to explore all the directions
        # calculate the new position the x and y axis
        # check if the new position is within grid
        # check if the new positions in the grid is not an obstacle
        # if no then calc new cost
        # add the new cost, new position and new move to queue

from heapq import heappush, heappop


def dijkstra_with_constraints(grid, start, destination, max_moves):
    # Define the directions (up, down, left, right, diagonal)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (-1, 1), (1, -1), (-1, -1)]

    # define a priority queue
    pq = []
    # add the first item to pq
    heappush(pq, (0, start, 0))

    # create a set to track visited positions
    visited = set()

    # run a loop until the queue is empty
    while pq:
        # pop the first item from priority queue
        cost, current_position, current_move_count = heappop(pq)

        # /******base cases to come out of the loop and return results *****/

        if (current_position == destination):
            return cost

        if current_position in visited or current_move_count > max_moves:
            continue

        visited.add(current_position)

        # explore all directions
        for dirx, diry in directions:
            # calc new positions in all directions
            x, y = current_position[0] + dirx , current_position[1] + diry
            # check if the new position is within the grid
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                # check if the current position is not an obstacle in the grid
                if (grid[x][y] != -1):
                    # calc new cost
                    new_cost = grid[x][y] + cost
                    # add to the queue
                    heappush(pq, (new_cost, (x, y), current_move_count + 1))
    return -1

# Example usage
grid = [
    [1, 3, 1, 2],
    [1, -1, 1, 5],
    [1, 3, 1, 7],
    [1, 4, 2, 1]
]
start = (0, 0)
destination = (3, 3)
max_moves = 6

min_cost = dijkstra_with_constraints(grid, start, destination, max_moves)
print("Minimum cost path:", min_cost)
