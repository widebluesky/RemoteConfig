#!/usr/bin/env python
"Remote Config Service Module"
import commands
from config import Constant
from util import FileUtil, JsonUtil
class RemoteConfigService(object):
    "File Util Class"
    def __init__(self):
        return
    def update_remote_config(self):
        "update remote config"
        if FileUtil.is_file_exists(Constant.GIT_LOCAL_PATH) != True:
            FileUtil.make_dirs(Constant.GIT_LOCAL_PATH)
        if FileUtil.is_file_exists(Constant.GIT_LOCAL_REPOSITORY_PATH) != True:
            gstr = 'git clone ' + Constant.GIT_REMOTE_URL + ' ' + Constant.GIT_LOCAL_REPOSITORY_PATH
            (status, output) = commands.getstatusoutput(gstr)
            print status
            print output
        self.update_config_file()
        self.update_remote_repository()
        return
        # if Constant.IS_TEST:
        #     socketutil = SocketUtil.SocketUtil()
        #     print socketutil.getfqdn()
        #     print socketutil.gethostbyname()
        # else:
        #     print "This is not a test"
        # return
    def update_config_file(self):
        "update config file"
        config_file_path = Constant.GIT_LOCAL_REPOSITORY_PATH + '/config.json'
        result_dic = {}
        result_dic['abc'] = 6632132167
        result_json = JsonUtil.dic_2_json(result_dic)
        result_file = open(config_file_path, 'wb')
        result_file.write(result_json)
        return
    def update_remote_repository(self):
        "update remote repository"
        (status, output) = commands.getstatusoutput('git --git-dir="' + Constant.GIT_LOCAL_REPOSITORY_PATH + '/.git" add *')
        (status, output) = commands.getstatusoutput('git --git-dir="' + Constant.GIT_LOCAL_REPOSITORY_PATH + '/.git" commit -m "333"')
        print status
        print output
        (status, output) = commands.getstatusoutput('git --git-dir="' + Constant.GIT_LOCAL_REPOSITORY_PATH + '/.git push --force')
        print status
        print output
        return

