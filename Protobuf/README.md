# Google Protocl Buffers Tutorial


Tutorial on how to use Google Protocol Buffers in Python for
  [Network Security](http://www.ccs.neu.edu/home/noubir/Courses/CS6740/S17/).

  **Instructor**: [Guevara Noubir](http://www.ccs.neu.edu/home/noubir)

  **Email**: noubir@ccs.neu.edu


## Requirements

 * Python 2.7
 * [Google Protocol Buffers](https://developers.google.com/protocol-buffers/docs/tutorials)

## Typical use

```
 $protoc --python_out=. pb-example.proto
```

 * In one terminal window run:
```
 $ ./socket-example-tcp-srv.py 
```
 * In another window run:
```
 $ ./socket-example-tcp-clt.py 
```

