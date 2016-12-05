#!/usr/bin/env python
"Main Module"
from service import RemoteConfigService

class Main(object):
    "Main Class"
    def __init__(self):
        return
    def excute(self):
        "excute Method"
        service = RemoteConfigService.RemoteConfigService()
        service.update_remote_config()
        return

if __name__ == "__main__":
    MAIN = Main()
    MAIN.excute()
