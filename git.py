#!/bin/bash
# encoding=utf-8
import os

exclude_files = ["1-01.Cocos2d-x启航.md", "1-02.使用Cocos2d-x.md", "1-03.低级错误大全.md", "README.md"]

for root, dirs, files in os.walk("./"):
    for file in files:
        if os.path.splitext(file)[1] == '.md':
            if file not in exclude_files and "基础卷" not in file:
                new  = file.replace(" ", "\ ")
                trim = " [基础卷]" + file.replace(" ", "")
                os.system("git mv \"" + new + "\"" + trim)