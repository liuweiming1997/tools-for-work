#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse

parser = argparse.ArgumentParser(description='manual to this script')

parser.add_argument('--floder', type=str, default='.')
parser.add_argument('--detail', type=bool, default=False)
parser.add_argument('--ignore_file', type=list, default=[])

args = parser.parse_args()

ignore_file_suffix = [".js"]
ignore_floder = [".git", "bin", "imgs"]

ans = "{\n"

def dfs_floder(root: str, name: str, tab: int):
    global ans
    path = os.path.join(root, name)
    for value in os.listdir(path):
        t_path = os.path.join(path, value)

        if os.path.isdir(t_path):
            if skip_floder(value):
                continue
        else:
            if skip_file(value):
                continue

        for i in range(0, tab + 1):
            ans += "  "
        ans += "'"
        ans += get_file_name(value)
        ans += "'"
        ans += ":"
        ans += "{"
        if os.path.isdir(t_path):
            ans += "\n"
            dfs_floder(path, value, tab + 1)
        for i in range(0, tab + 1):
            ans += "  "
        ans += "},"
        ans += "\n"


def get_file_name(value: str) -> 'str':
    return os.path.splitext(value)[0]

def skip_floder(file_name: str) -> 'boolean':
    return file_name in ignore_floder

def skip_file(file_name: str) -> 'boolean':
    suffix = os.path.splitext(file_name)[-1]
    if suffix == "":
        suffix = os.path.splitext(file_name)[-2]
    return suffix not in ignore_file_suffix

dfs_floder(args.floder, '', 0)
ans += "}"
print(ans)