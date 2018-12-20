#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import csv
import random
import string

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--file', type=str, default='xxx.csv', help="The file you want to parse")
args = parser.parse_args()

data = {}
secret_key = ''.join(random.sample(string.ascii_letters + string.digits, 24))
tab_string = "  "

def is_empty_line(item: list) -> 'bool':
    for value in item:
        if value:
            return False
    return True

def parse_csv_to_dict(file) -> 'void':
    pre_item = []
    csv_reader = csv.reader(file)
    for item in csv_reader:
        d = data
        if is_empty_line(item):
            continue
        if item[0]:
            pre_item = item
        for idx in range(0, len(item)):
            if item[idx]:
                pre_item[idx] = item[idx]
                if idx == len(item) - 1 or item[idx + 1] == '':
                    d[secret_key] = item[idx]
                    break
                else:
                    if item[idx] in d.keys():
                        d = d[item[idx]]
                    else:
                        d[item[idx]] = {}
                        d = d[item[idx]]
            else:
                d = d[pre_item[idx]]

result = '{\n'

def parse_dict_to_json(d: dict, tab_num: int) -> 'void':
    global result
    for key in sorted(d):
        for i in range(0, tab_num):
            result += tab_string
        result += "'{0}': ".format(key)

        if secret_key in d[key]:
            result += "'{0}',\n".format(d[key][secret_key])
            continue
        else:
            result += "{\n"
        parse_dict_to_json(d[key], tab_num + 1)
        for i in range(tab_num):
            result += tab_string
        result += "},\n"

with open(args.file) as file:
    parse_csv_to_dict(file)
    parse_dict_to_json(data, 1)
    result += "}\n"
    print(result)
