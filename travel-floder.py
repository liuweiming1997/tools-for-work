# -*- coding: utf-8 -*-

import os
import argparse

parser = argparse.ArgumentParser(description='manual to this script')

parser.add_argument('--floder', type=str, default='.')
parser.add_argument('--detail', type=bool, default=False)
parser.add_argument('--ignore_file', type=list, default=[])

args = parser.parse_args()

ignore_file_suffix = [".gitignore", ".md"]
ignore_floder = [".git", "bin", "imgs"]

def travel_floder(root: str, name: str):
    path = os.path.join(root, name)
    if os.path.isdir(path) == False:
        if skip_file(name) == False:
            handle_file(path)
        return
    else: # floder
        if skip_floder(name):
            return

    for value in os.listdir(path):
        travel_floder(path, value)


def skip_floder(file_name: str) -> 'boolean':
    return file_name in ignore_floder

def skip_file(file_name: str) -> 'boolean':
    suffix = os.path.splitext(file_name)[-1]
    if suffix == "":
        suffix = os.path.splitext(file_name)[-2]
    return suffix in ignore_file_suffix

def contain_zh_hans(word: str) -> 'boolean':
    import re
    zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zh_pattern.search(word)
    return match

def handle_file(file_name: str):
    with open(file_name, 'rt') as f:
        for line in f:
            if contain_zh_hans(line):
                if args.detail:
                    print(file_name + ' --> ' + line[:-1])
                else:
                    print(file_name)
                return

travel_floder(args.floder, '')
