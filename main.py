#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: main.py
@time: 27/01/2018 10:00
"""

import os
import sys
import argparse
import requests
import hashlib
import time
from storage import driver


parser = argparse.ArgumentParser(description="This script is mean to transfor your latex function "
                                             "to image tag in markdown format automatically")

parser.add_argument('-i', '--input', dest='input', required=True, help='the directory of file that need to process')
parser.add_argument('-o', '--output', dest='output', help='the directory where store processed file')


def process_tag(tag_str):
    func = tag_str[2:-2]
    storage = driver.resolve()
    remote_img = 'http://latex.codecogs.com/gif.latex?%s' % func
    r = requests.get(remote_img)
    local_img = '/Users/william/Downloads/%d' % time.time()
    with open(local_img, 'wb+') as f:
        f.write(r.content)
    url = storage.put(local_img)
    return '![](%s)' % url



def handle(filename, outfile):
    with open(filename) as f:
        content = f.read()
        last_idx = 0
        matched = False
        res = ""
        idx1 = -1
        idx2 = -1
        while True:
            idx1 = content.find('$$', last_idx)
            if idx1 < 0:
                break
            idx2 = content.find('$$', idx1 + 1)
            res += content[last_idx:idx1]
            res += process_tag(content[idx1:idx2+2])
            last_idx = idx2 + 2
        if idx2 >= 0:
            res += content[idx2:]
        out = open(outfile, 'a+')
        out.write(res)
        out.close()


if __name__ == '__main__':
    args = parser.parse_args()
    storage = driver.resolve()
    input = args.input
    is_file = os.path.isfile(input)
    if args.output:
        output = args.output
    else:
        output = input if not is_file else os.path.split(input)[0]

    if is_file:
        # TODO process one file
        pass

    else:
        for parent, dirs, files in os.walk(input):
            for file in files:
                if file[-3:] != '.md':
                    continue
                full_path = os.path.join(parent, file)
                outfile = os.path.join(output, file)
                i = 0
                while os.path.exists(outfile):
                    outfile = os.path.join(output, "%s_%d.md" % (file[:-3], i))
                    i += 1
                    if i > 99:
                        raise Exception('Can\'t find a unique name for [%s]' % file)
                handle(full_path, outfile)





