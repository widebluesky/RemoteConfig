#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"Main Module"
import time
from service import RemoteConfigService
from util import LogUtil

class Main(object):
    "Main Class"
    def __init__(self):
        return
    def excute(self):
        "excute Method"
        service = RemoteConfigService.RemoteConfigService()
        while True:
            current_time = time.strftime('%Y-%m-%d %X', time.localtime())
            LogUtil.print_i('Excute RemoteConfig update at ' + current_time)
            service.update_remote_config()
            time.sleep(60)
        return

if __name__ == "__main__":
    MAIN = Main()
    MAIN.excute()
