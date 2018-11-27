import numpy as np

class Utilities(object):

	# Creating a NxM array with 1 as dust, 0 otherwise (we don't need to
	# save the position of the robot in the matrix)
	@classmethod
	def create_and_populate_map(self, problem):
	    robot_world_arr = np.zeros((problem['roomSize'][0],problem['roomSize'][1]))
	    for patch in problem["patches"]:
	        robot_world_arr[patch[0]][patch[1]] = 1
	    # When putting in the robot, if it's put in a position with 1 in it, we 
	    # start counting our dust removals from 1 not zero.
	    dust_count = 0
	    if robot_world_arr[problem['coords'][0]][problem['coords'][1]] == 1:
	        dust_count+=1
	    robot_world_arr[problem['coords'][0]][problem['coords'][1]] = 0

	    return robot_world_arr, dust_count

	def isInside(robot_world_arr, current_pos, row, col):
	    if current_pos[0]+row < 0 or current_pos[0]+row >= robot_world_arr.shape[0] \
	       or current_pos[1]+col < 0 or current_pos[1]+col >= robot_world_arr.shape[1]:
	       return False
	    return True

	# Returns the next move coordinates
	def grab_move(c):
	    if c == "S":
	        return -1, 0
	    elif c == "N":
	        return 1, 0
	    elif c == "E":
	        return 0, 1
	    elif c == "W":
	        return 0, -1
	    else:
	        return None, None

	@classmethod
	def calculate_final_pos_and_dirt_patches(self, problem, robot_world_arr, dust_count):
	    current_pos = problem["coords"]
	    for c in problem["instructions"]:
	        row_move, col_move = self.grab_move(c)
	        if row_move is None:
	            # We just skip invalid characters
	            continue
	        if self.isInside(robot_world_arr, current_pos, row_move, col_move):
	            if robot_world_arr[current_pos[0] + row_move][current_pos[1] + col_move] == 1:
	                dust_count+=1
	                robot_world_arr[current_pos[0] + row_move][current_pos[1] + col_move] = 0
	            if row_move == 0:
	                # it's a column move
	                current_pos[1] = current_pos[1] + col_move
	            else:
	                current_pos[0] = current_pos[0] + row_move
	    return {"coords" : current_pos, "patches" : dust_count}