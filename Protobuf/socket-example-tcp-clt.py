#!/usr/bin/env python

# A very basic program demonstrating protobuf with sockets
# Note that it does not catch any exceptions and of course 
# it is very insecure as executes remote commands :)
#
# This is the client side

__author__      = "Guevara Noubir"

import socket
import time
import pb_example_pb2 	# import the module created by protobuf
						# for creating messages



IP_ADDR = '127.0.0.1'	# use loopback interface
TCP_PORT = 5055			# TCP port of server
BUFFER_SIZE = 1024

rqst = pb_example_pb2.Request()	# create protobuf Request message
rply = pb_example_pb2.Reply()	# create protobuf Reply message

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP_ADDR, TCP_PORT))	# connect to server

reqno = 0				# initialize request number to 0

for reqno in range(100):	# send 100 requests

    rqst.version = 7		# this is arbitrary for illustration purpose
    rqst.seqn = reqno		# set sequence number

							# get request type from user
    rcmd = raw_input('Request Type (1: ECHO, 2: RCMD): ')

    if rcmd == '1':			# will generate an ECHO request
        rqst.type = pb_example_pb2.Request.ECHO

        # payload is an arbitrary string for ECHO
        rqst.payload = raw_input('Your text to be echoed: ')

    elif rcmd == '2':		# will generate a request to execure a command on server
        rqst.type = pb_example_pb2.Request.RCMD

        # payload is a command to be executed on server
        rqst.payload = raw_input('Command to execute on server: ')        

    else:
        print "Unknown command"
        continue



    # serialize message to string
    sock.send(rqst.SerializeToString())

    # read response
    data = sock.recv(BUFFER_SIZE)

    # parse response message
    rply.ParseFromString(data)

    # print fields of response
    print "received data... ", rply.version, rply.seqn, rply.payload

sock.close() # close socket

