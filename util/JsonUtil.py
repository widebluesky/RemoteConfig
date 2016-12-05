#!/usr/bin/env python
"Json Util Module"
import json
class JsonUtil(object):
    "File Util Class"
    def __init__(self):
        return
def dic_2_json(dic):
    "dic 2 json "
    return json.dumps(dic, encoding='utf-8').decode('utf-8')
def json_file_2_dic(file_path):
    "json file 2 dic"
    return json.loads(open(file_path).read(), encoding='utf-8')
    