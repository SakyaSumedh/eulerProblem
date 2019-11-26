'''
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

def number_of_routes(x_grid, y_grid):
	# solution 1
	'''
	Using matrix form
	'''
	# grid = [[0 for i in range(x_grid + 1)] for j in range(y_grid + 1)]
	#
	# for i in range(x_grid + 1):
	# 	for j in range(y_grid + 1):
	# 		if i == 0 or j == 0:
	# 			grid[i][j] = 1
	# 			continue
	# 		grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
	# return grid[x_grid][y_grid]

	# solution 2
	'''
	Fully optimized
	Using combination as
	(X+Y X) or (X+Y Y) = (n k) = n! / (k! * (n - k)!)
	'''
	from math import factorial
	return factorial(x_grid + y_grid) / (factorial(x_grid) * factorial(y_grid))

import time
start = time.time()
print(int(number_of_routes(200, 200)))
print(time.time() - start)
