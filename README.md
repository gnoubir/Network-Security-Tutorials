# Network-Security-Tutorials

- [Network-Security-Tutorials](#network-security-tutorials)
  - [Quick Start](#quick-start)
    - [MacOS](#macos)
  - [Google Protocol Buffers with sockets](#google-protocol-buffers-with-sockets)
  - [ZeroMQ with Sockets](#zeromq-with-sockets)
  - [Crypto in Python](#crypto-in-python)
  - [Basic Cryptanalysis](#basic-cryptanalysis)
  - [Instant Messaging Base Code](#instant-messaging-base-code)

## Quick Start

### MacOS

```bash
brew install protobuff
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt 
```

This repository provides several samples of code that might be useful for your Network Security problem sets and project.

## Google Protocol Buffers with sockets

Some sample code on how to use Google protobuf to create and parse messages for network communications.

## ZeroMQ with Sockets

Some sample code for networked communications using basic ZMQ patterns.

## Crypto in Python

Some sample python code demonstrating a variety of cryptographic building blocks (e.g., hashing, encryption, integrity protection). 

## Basic Cryptanalysis

A very basic statistical analysis tool of text illustrating English (or other languages) letters distribution.

## Instant Messaging Base Code

A basic instant messaging applications using ZMQ and some limited use of google protobuf, supporting REGISTER, LIST, and SEND commands. Note that you need to spend some time to understand how ZMQ DEALER - ROUTER communication pattern works. 
