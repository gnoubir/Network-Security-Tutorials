

You first need to generate the python code from proto definition file of google protobuf:

```
 $protoc --python_out=. messaging-app.proto
 ```
 
 Run the server using the following command (note that you can specify the port see --help output):
 
```
 ./server-im.py
```
 
 Run the client using the following command (note that you can specify the server IP address, port, and username see --help output):
 
```
 ./client-im.py -u Alice
```
and on another terminal:

```
 ./client-im.py -u Bob
```

 Use the ```LIST``` command and ```SEND Alice Hello there!``` to test.
 
 
 
