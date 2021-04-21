#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2021/04/21 16:52:44
@Desc    :   None
'''

# here put the import lib
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer


class EchoServer(TCPServer):
    async def handle_stream(self, stream, address):
        while True:
            try:
                data = await stream.read_until(b"\n")
                print("recv msg: ", data)
                await stream.write(data.upper())
            except Exception as e:
                print("lost connection at {}".format(address[0]))
                break

if __name__ == "__main__":
    port = 9888
    server = EchoServer()
    server.listen(port)
    print("Listening on tcp port {}".format(port))
    IOLoop.current().start()
