#!/usr/bin/env python

import http.client
import json

# Here we can call generate_test_case.py grab the result
# and send it as a request to the server and then read the 
# result in an iterative fashion instead of doing it one by one

conn = http.client.HTTPConnection('localhost', 8080)

headers = {'Content-type': 'application/json'}

test_case_1 = {"roomSize" : [5, 5],\
			   "coords" : [1, 2],\
			   "patches" : [[1, 0], [2, 2], [2, 3]],\
  			   "instructions" : "NNESEESWNWW"
}

test_case_2 = {'roomSize': [9, 11], 'coords': [3, 7],\
			   'instructions': 'SNWWWNSNWSSENNNENSSSNEWNESNESNNW',\
			   'patches': [[6, 5], [4, 6], [3, 0], [1, 3]]}
#foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
json_data = json.dumps(test_case_1)

conn.request('POST', '/', json_data, headers)
print("Sending test case = %s"%test_case_1)
response = conn.getresponse()
if response.status == 200:
	print("Got 200 status.")
	if response.reason:
		print("Reason = %s"%response.reason)
		print("Result = %s"%response.read().decode('utf-8'))
else:
	print("Got %d status"%response.status)
	if response.reason:
		print("Reason = %s"%response.reason)
