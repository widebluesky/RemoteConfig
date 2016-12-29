#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"Remote Config Service Module"
import os
import time
import commands
from config import Constant
from util import FileUtil, JsonUtil, SocketUtil, LogUtil
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
        update_config_success = self.update_config_file()
        if update_config_success:
            self.update_remote_repository()
        return
    def update_config_file(self):
        "update config file"
        config_file_path = Constant.GIT_LOCAL_CONFIG_FILE_PATH
        local_config_dic = JsonUtil.json_file_2_dic(config_file_path)
        result_config_dic = self.get_result_dic()
        local_config_json = JsonUtil.dic_2_json(local_config_dic)
        result_config_json = JsonUtil.dic_2_json(result_config_dic)
	if local_config_json == result_config_json:
            LogUtil.print_e('nothing need to update')
            return True
        result_file = open(config_file_path, 'wb')
        result_file.write(result_config_json)
        return True
    def update_remote_repository(self):
        "更新远程仓库"
        os.chdir(Constant.GIT_LOCAL_REPOSITORY_PATH)
        local_time = time.localtime(time.time())
        local_time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        git_add_str = 'git add *'
        git_commit_str = 'git commit -m "Auto Commit Time ' + local_time_str + '"'
        git_push_str = 'git push --force'
        # add 更新文件
        (status, output) = commands.getstatusoutput(git_add_str)
        # commit 文件提交本地
        (status, output) = commands.getstatusoutput(git_commit_str)
        # push 远程仓库
        (status, output) = commands.getstatusoutput(git_push_str)
        if status == 0:
            LogUtil.print_i(output)
            LogUtil.print_i('success')
        else:
            LogUtil.print_e(output)
            LogUtil.print_e('error')
        return
    def get_result_dic(self):
        "get result dic"
        result_dic = {}
        result_dic['version'] = '1.0.1'
        server_info = {}
        server_info['ip_local'] = SocketUtil.SocketUtil().get_host_by_name()
        server_info['ip_remote'] = SocketUtil.SocketUtil().get_internet_ip_address()
        result_dic['server_info'] = server_info
        return result_dic
    def validate_version(self, old_version, new_version):
        "版本号检测"
        if not old_version.find('.'):
            return False
        if not new_version.find('.'):
            return False
        new_version_code = new_version.replace('.', '')
        old_version_code = old_version.replace('.', '')
        if new_version_code > old_version_code:
            return True
        else:
            return False
