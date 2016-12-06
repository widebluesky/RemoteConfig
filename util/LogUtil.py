#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"Log Util Module"
class LogUtil(object):
    "Log Util Class"
    def __init__(self):
        return
def print_e(message):
    "log error"
    print '[Error]' + message
    return
def print_w(message):
    "log warning"
    print '[Warn]' + message
    return
def print_i(message):
    "log info"
    print '[Info]' + message
    return
def print_d(message):
    "log debug"
    print '[Debug]' + message
    return