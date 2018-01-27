#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: driver.py
@time: 27/01/2018 00:13
"""


from core import config

__drivers = {}
__default_name = config.get('storage.use')
_driver = __import__(__default_name)


def bind(name, instance):
    __drivers[name] = instance


def resolve(name=None):
    if name is None:
        name = __default_name
    if name in __drivers:
        return __drivers[name]
    else:
        raise Exception('Unregistered storage driver [%s]' % name)


def create_instance(class_name, *args, **kwargs):
    (module_name, class_name) = class_name.rsplit('.', 1)
    module_meta = __import__(module_name, globals(), locals(), [class_name])
    class_meta = getattr(module_meta, class_name)
    return class_meta(*args, **kwargs)


_class_name = __default_name.capitalize()
bind(__default_name, create_instance('storage.%s.%s' % (__default_name, _class_name),
                                     config.get('storage.' + __default_name)))
