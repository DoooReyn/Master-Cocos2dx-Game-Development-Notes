#!/bin/bash
# encoding=utf-8
import os

exclude_files = ["README.md"]

for root, dirs, files in os.walk("./"):
    for file in files:
        if os.path.splitext(file)[1] == '.md':
            if file not in exclude_files and "基础卷" not in file:
                new  = file.replace(" ", "\ ")
                trim = " [基础卷]" + file.replace(" ", "")
                os.system("git mv \"" + new + "\"" + trim)