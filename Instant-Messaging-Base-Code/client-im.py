#!/usr/bin/env python
#
'''
Simple Chat Program that allows users to register, request the list of registered users,
and send a message to another user through the server. This code can get you started with
your CS4740/6740 project.

Note, that a better implementation would use google protobuf more extensively, with a 
single message integrating both control information such as command type and other fields.
See the other provided tutorial on Google Protobuf.

Also, note that the services provided by this sample project do not nessarily satify the
functionality requirements of your final instant messaging project.
'''

__author__      = "Guevara Noubir"

import zmq
import sys
import time
import base64
import argparse

import messaging_app_pb2

NOT_REGISTERED = 0
REGISTERED = 1


parser = argparse.ArgumentParser()

parser.add_argument("-s", "--server",
                    default="localhost",
                    help="Server IP address or name")

parser.add_argument("-p", "--server-port", type=int,
                    default=5569,
                    help="port number of server to connect to")

parser.add_argument("-u", "--user",
                    default="Alice",
                    help="name of user")

args = parser.parse_args()


#  Prepare our context and sockets
context = zmq.Context()

# We are using the DEALER - ROUTER pattern see ZMQ docs
socket = context.socket(zmq.DEALER)
socket.connect("tcp://%s:%s" %(args.server, args.server_port))

# Set username based on args parameters from the command line or default
username = args.user

# Initialize state of client
status = NOT_REGISTERED

# Function to print a prompt character
def print_prompt(c):
    sys.stdout.write(c)
    sys.stdout.flush()

# Create the google protopub message -- format is defined in messaging-app.proto
# This is in some sense for illustration what you can do with protbub
user = messaging_app_pb2.User()

# Set username field in user message
user.name = username

# Send REGISTER message to server
# Use the send_multipart API of ZMQ -- again to illustrate some of the capabilities of ZMQ
socket.send_multipart([b"REGISTER", username, user.SerializeToString()])

# An alternative would have been to send the usernam directly 
#socket.send_multipart([b"REGISTER", username])

# We are going to wait on both the socket for messages and stdin for command line input
poll = zmq.Poller()
poll.register(socket, zmq.POLLIN)
poll.register(sys.stdin, zmq.POLLIN)


while(True):
    sock = dict(poll.poll())

    # if message came on the socket
    if socket in sock and sock[socket] == zmq.POLLIN:
        message = socket.recv_multipart()

        # If LIST command
        if message[0] == 'LIST' and len(message) > 1:
            d = base64.b64decode(message[1])
            print("\n  - Currently logged on: %s\n" % (d))
            print_prompt(' <- ')

        # If MSG 
        if message[0] == 'MSG' and len(message) > 1:
            d = message[1] #base64.b64decode(message[1])
            print("\n  > %s" % (d))
            print_prompt(' <- ')    

        # If response to the REGISTER message
        if message[0] == 'REGISTER' and len(message) > 1:
            d = message[1] #base64.b64decode(message[1])
            print("\n <o> %s" % (d))
            print_prompt(' <- ')

        # If error encountered by server
        if message[0] == 'ERR' and len(message) > 1:
            d = message[1] #base64.b64decode(message[1])
            print("\n <!> %s" % (d))
            print_prompt(' <- ')

    # if input on stdin -- process user commands
    elif sys.stdin.fileno() in sock and sock[0] == zmq.POLLIN:
        userin = sys.stdin.readline().splitlines()[0]
        print_prompt(' <- ')

        # get the first work on user input
        cmd = userin.split(' ', 2)

        # if it's list send "LIST", note that we should have used google protobuf
        if cmd[0] == 'LIST':
            socket.send(b"LIST")

        # A user can issue a register command at anytime, although not very useful
        #  since client sends the REGISTER message automatically when started
        if cmd[0] == 'REGISTER':
            user = messaging_app_pb2.User()
            user.name = username

            # Note that the username is sent both without and with protobuf
            socket.send_multipart([b"REGISTER", username, user.SerializeToString()])

        # SEND command is sent as a three parts ZMQ message, as "SEND destination message"
        elif cmd[0] == 'SEND' and len(cmd) > 2:
            socket.send_multipart([cmd[0], cmd[1], cmd[2]])
  
