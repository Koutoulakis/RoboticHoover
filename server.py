#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
from utilities import Utilities
import simplejson
import json
import traceback


# I'd like to do this in java, but the quickest way to start a simple http server is 
# provided by python and nodejs. I went for python out of those two as I thought it was quicker.

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_error(404, 'Not supported yet.')
        
    def do_POST(self):
        
        print("In post method")
        
        request_path = self.path
        request_headers = self.headers
        if request_path == "/":
            # We could answer immediately and
            try:
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length)
                problem = simplejson.loads(body)
                if "roomSize" and "patches" and "coords" and "instructions" in problem:
                    robot_world_arr, dust_count = Utilities.create_and_populate_map(problem)

                    res_json = Utilities.calculate_final_pos_and_dirt_patches(problem, robot_world_arr, dust_count)
                    self.send_response(200,  "success")
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(res_json).encode('utf-8'))
                    print("Request completed successfully")
                else:
                    self.send_error(500, 'Not all necessary parameters were provided!')
                    print("Request without the necessary parameters was provided")
                return
            except Exception as e:
                print(e)
                traceback.print_exc()
                self.send_error(400, 'Oops, something went wrong, try again later.')
        else:
            self.send_error(404, request_path + ' is not supported yet, use / instead')
            print("Request with invalid url(%s) was provided."%request_path)
            return
    
    do_PUT = do_GET
    do_DELETE = do_GET

        
if __name__ == "__main__":
    try:
        port = 8080
        print('Listening on localhost:%s' % port)
        server = HTTPServer(('', port), RequestHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print ('Keyboard interrupt received, shutting down web server')
        server.socket.close()