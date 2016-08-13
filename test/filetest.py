#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
"""

import os,shutil

print u"Python 是一个非常棒的语言，不是吗？";

fo = open("D:\\Main.java" ,"r+")


print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace


lines = []
for line in fo: # 内置的迭代器, 效率很高
    lines.append(line)

lines.insert(0, 'a new line\n') # 在第二行插入
s = ''.join(lines)
print s
fo.seek(0,0)
fo.write(s)
fo.close()
