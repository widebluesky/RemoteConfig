#!/usr/bin/env python
"Socket Util Module"
import socket
class SocketUtil(object):
    "Socket Util Class"
    def __init__(self):
        return
    def gethostname(self):
        "Get Host Name Method"
        return socket.gethostname()
    def getfqdn(self):
        "Get fqdn Method"
        return socket.getfqdn(self.gethostname())
    def gethostbyname(self):
        "Get Host By Name Method"
        return socket.gethostbyname(self.getfqdn())

#class Main(object):
#    "Main Class"
#    def __init__(self):
#        return
#    def excute(self):
#        "excute Method"
#        socketutil = SocketUtil()
#        print socketutil.getfqdn()
#        print socketutil.gethostbyname()
#        return

#if __name__ == "__main__":
#    MAIN = Main()
#    MAIN.excute()
   