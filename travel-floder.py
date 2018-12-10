# -*- coding: utf-8 -*-

import os

import argparse
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--floder', type=str, default='.')
args = parser.parse_args()
# print (args.batch_size)

ignore_file_suffix = [".gitignore", ".md"]
ignore_floder = [".git"]

def travel_floder(root: str, file_name: str):
    path = os.path.join(root, file_name)
    if os.path.isdir(path) == False:
        if skip_file(file_name) == False:
            handle_file(path)
        return
    else: # floder
        if (skip_floder(path)):
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

def handle_file(file_name: str):
    print(file_name)

travel_floder(args.floder, '')
