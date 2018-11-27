#!/usr/bin/env python
import random
import math

# This can be done iteratively and save it in a gzip file that
# Can then be read from a client and send as multiple requests
# to the server.

print("Starting test case generation")

def generate_instructions(directions, number_of_moves):
	res = ""
	for i in range(0, number_of_moves, 1):
		res += random.choice(directions)
	return res

def generate_patches(patches_no, rows, cols):
	patches = []
	for i in range(0, patches_no, 1):
		# We don't care if it's in the same spot as the hoover. It will
		# clean it automatically without moving
		patches.append([random.randint(0,rows-1), random.randint(0,cols-1)])
	return patches

# We will make random input cases with a max 15x15 array
# the number of patches is a  random number between 0 and 1/3 of 15*15
directions = ['N', 'S', 'W', 'E']
rows = random.randint(5,15)
cols = random.randint(5,15)
coord_row = random.randint(0,rows-1)
coord_col = random.randint(0,cols-1)

patches_no = random.randint(0, math.ceil(rows*cols/3))

# It can contain duplicates, but we don't care
patches = generate_patches(patches_no, rows, cols)
instructions = generate_instructions(directions, random.randint(1,math.ceil(rows*cols/3)))

test_case = {"roomSize": [rows, cols], "coords": [coord_row, coord_col],\
             "patches": patches, "instructions": instructions}

print("test case = %s"%test_case)
print("Test case generated!")