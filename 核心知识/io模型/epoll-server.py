#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   epoll-server.py
@Time    :   2021/04/20 19:56:48
@Desc    :   None
'''

# here put the import lib
import socket
import select


def serve():
    server = socket.socket()
    server.bind(("127.0.0.1", 8999))
    server.listen(1)

    epoll = select.epoll()
    # epoll = select.kqueue()
    epoll.register(server.fileno(), select.EPOLLIN)

    connections = {}
    contents = {}

    while True:
        events = epoll.poll(10)

        for fileno, event in events:
            # 说明有新连接进来了
            if fileno == server.fileno():
                s, addr = server.accept()
                print("new connection from addr:", addr)
                epoll.register(s.fileno(), select.EPOLLIN)
                connections[s.fileno()] = s
            # 有数据可读
            elif event == select.EPOLLIN:
                s = connections[fileno]
                content = s.recv(1024)
                # 关闭连接
                if not content:
                    epoll.unregister(fileno)
                    s.close()
                    connections.pop(s.fileno())
                else:
                    content = content.upper()
                    # 改为关注写事件
                    epoll.modify(fileno, select.EPOLLOUT)
                    contents[fileno] = content
            # 写事件就绪
            elif event == select.EPOLLOUT:   
                try: # 捕获网络中断异常
                    content = contents[fileno]
                    s = connections[fileno]
                    s.send(content)
                    epoll.modify(fileno, select.EPOLLIN)
                except:
                    epoll.unregister(fileno)
                    s.close()
                    connections.pop(fileno)
                    contents.pop(fileno)


if __name__ == "__main__":
    serve()