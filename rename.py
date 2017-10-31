#!/bin/bash
# encoding=utf-8
import os

exclude_files = ["README.md"]

for item in os.listdir('./'):
    if os.path.isfile(item) \
    and os.path.splitext(item)[1] == '.md' \
    and item not in exclude_files \
    and "基础卷" not in item:
        trim = " [基础卷]"+item
        print("git mv {0} {1}".format(item, trim))