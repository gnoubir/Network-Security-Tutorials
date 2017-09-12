#!/usr/bin/env python
#
# A very basic program demonstrating protobuf with sockets
# Note that it does not catch any exceptions and of course 
# it is very insecure as executes remote commands :)
#
# This is the server side

__author__      = "Guevara Noubir"

import socket
import time
import sys
import pb_example_pb2 	# import the module created by protobuf
						# for creating messages
import subprocess    	# module for executing commands from python
						# and retrieving stdout


IP_ADDR = '127.0.0.1'	# use loopback interface
TCP_PORT = 5055			# TCP port of server
BUFFER_SIZE = 1024

rqst = pb_example_pb2.Request()	# create protobuf Request message
rply = pb_example_pb2.Reply()	# create protobuf Reply message

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((IP_ADDR, TCP_PORT))	# bind to port

sock.listen(1)			# listen with one pending connection

conn, addr = sock.accept()	# accept connection from client

print 'Connection address:', addr

while 1:				# process one request at a time
    data = conn.recv(BUFFER_SIZE)
    if not data: break

    print "received data..."

    rqst.ParseFromString(data)	# parse message
    print rqst.version, rqst.seqn	# print version and sequence number

    if rqst.version != 7:		# only accept version 7
    	continue

    rply.version = rqst.version	# use same version number for reply

    rply.seqn = rqst.seqn       # use same version number for reply

    if (rqst.type == pb_example_pb2.Request.ECHO): # echo request
    	rply.payload = rqst.payload                # just copy payload

    if (rqst.type == pb_example_pb2.Request.RCMD):  # remote command request
    	print 'Executing command: ', rqst.payload
                                                    # execute command and get stdout
    	rply.payload = subprocess.check_output(rqst.payload, shell='True')

    conn.send(rply.SerializeToString())  # serialize response into string and send
    
conn.close()