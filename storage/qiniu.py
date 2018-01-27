#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: qiniu.py
@time: 26/01/2018 23:52
"""
import os
from qiniu import Auth, put_file


class Qiniu(object):
    __q = None
    __prefix = None
    __bucket = None
    __domain = None

    def __init__(self, config):
        assert 'access_key' in config
        assert 'secret_key' in config
        assert 'bucket' in config
        assert 'domain' in config
        self.__q = Auth(config['access_key'], config['secret_key'])
        self.__bucket = config['bucket']
        self.__prefix = config['prefix'] if 'prefix' in config else ''
        self.__domain = config['domain']
        if self.__domain[-1] != '/':
            self.__domain += '/'

    def put(self, localfile):
        name = os.path.split(localfile)[1]
        key = self.__prefix + name
        token = self.__q.upload_token(self.__bucket, key)
        ret, info = put_file(token, key, localfile)
        print(ret, info)
        return self.__domain + key


