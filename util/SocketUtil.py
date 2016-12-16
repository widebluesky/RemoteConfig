#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"Socket Util Module"
import re
import socket
import urllib2
class SocketUtil(object):
    "Socket Util Class"
    def __init__(self):
        return
    def get_hostname(self):
        "Get Host Name Method"
        return socket.gethostname()
    def get_fqdn(self):
        "Get fqdn Method"
        return socket.getfqdn(self.get_hostname())
    def get_host_by_name(self):
        "Get Host By Name Method"
        return socket.gethostbyname(self.get_fqdn())
    def get_internet_ip_address(self):
        "Get Internet IP Address Method"
        response = urllib2.urlopen('http://www.ip.cn')
        html = response.read()
        ip_address = re.search(r'code.(.*?)..code', html)
        return ip_address.group(1)
    def get_local_ip_address(self):
        "Get Local IP Address Method"
        try:
            csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            csock.connect(('8.8.8.8', 80))
            (addr, port) = csock.getsockname()
            csock.close()
            return addr
        except socket.error:
            return "127.0.0.1"
    def get_internet_ip_address2(self):
        try:
            myip = self.visit("http://www.whereismyip.com/")
        except:
            try:
                myip = self.visit("http://www.ip138.com/ip2city.asp")
            except:
                myip = "So sorry!!!"
        return myip
    def visit(self,url):
        opener = urllib2.urlopen(url)
        if url == opener.geturl():
            str = opener.read()
        return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)

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
   