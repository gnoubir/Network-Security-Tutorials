#!/usr/bin/env python
#
'''
Simple Chat Program that allows users to register, request the list of registered users,
and send a message to another user through the server. This code can get you started with
your CS4740/6740 project.

Note, that a better implementation would use google protobuf more extensively, with a 
single message integrating both control information such as command type and other fields.
See the other provided tutorial on Google Protobuf.

Also, note that the services provided by this sample project do not nessarily satisfy the
functionality requirements of your final instant messaging project.

Finally, we use DEALER and ROUTER to be able to communicate back and forth with multiple 
clients (ROUTER remembers identities [first part of message] when it receives a message and
prepends identity to messages when sending to DEALER). See:
  http://zguide.zeromq.org/php:chapter3.
'''

__author__      = "Guevara Noubir"


import zmq
import sys
import time
import base64
import argparse

import messaging_app_pb2


parser = argparse.ArgumentParser()

parser.add_argument("-p", "--server-port", type=int,
                    default=5569,
                    help="port number of server to connect to")

args = parser.parse_args()

#  Prepare our context and sockets
context = zmq.Context()

# We are using the DEALER - ROUTER pattern see ZMQ docs
socket = context.socket(zmq.ROUTER)
socket.bind("tcp://*:%s" %(args.server_port))

# store registered users in a dictionary
logged_users = dict()
logged_ident = dict()

# main loop waiting for users messages
while(True):

    
    message = socket.recv_multipart()

    # Remeber that when a ROUTER receives a message the first part is an identifier 
    #  to keep track of who sent the message and be able to send back messages
    ident = message[0]

    print("Received [%s]" % (message[1]))

    if len(message) == 2:
    	if message[1]== 'LIST':

            # If first seeing this identity sent back ERR message requesting a REGISTER
    		if ident not in logged_ident:
    			socket.send_multipart([ident, b'ERR', b'You need to register first.'])
    		else:

	    		print("List request from user %s" %(logged_ident[ident]))
    			socket.send_multipart([ident, b'LIST', base64.b64encode(str(logged_users))])

    if len(message) == 4:
    	if message[1] == 'REGISTER':
    		logged_users[message[2]] = ident
    		logged_ident[ident] = message[2]
    		user = messaging_app_pb2.User()
    		user.ParseFromString(message[3])
    		print ("Registering %s" % (user.name))
    		socket.send_multipart([ident, b"REGISTER", b'Welcome %s!' %(str(user.name))])

    if len(message) == 4:
    	if message[1] == 'SEND':
    		# check if destination is registered, retrieve address, and forward
    		if message[2] in logged_users:
    			print "sending message to %s" %(message[2])

                # Note that message from ROUTER is prepended by destination ident 
    			socket.send_multipart([logged_users[message[2]], b'MSG', message[3]])
    		else:
    			socket.send_multipart([ident, b'ERR', message[2] + b' not registered.'])
    