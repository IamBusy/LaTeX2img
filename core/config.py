#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: config.py
@time: 26/01/2018 23:53
"""

import toml
import os

APP_PATH = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

__config = toml.load(os.path.join(APP_PATH, 'config.toml'))


def get(key_str, def_val=None):
    cur = __config
    try:
        for key in key_str.split('.'):
            cur = cur[key]
        return cur
    except Exception as e:
        return def_val
