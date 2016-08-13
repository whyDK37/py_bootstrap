#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
"""

import os,shutil

print u"Python 是一个非常棒的语言，不是吗？";



package = U"D:\\workspace\\mygit\\pinenut\\java-core\\DesignPatterns\\src\\main\\java\\"

patterns = os.listdir(package)
for index in range(len(patterns)):
    pattern = patterns[index];
    pattern_root = package+pattern
    print(u"pattern: "+  pattern_root)
    patternfiles = os.listdir(pattern_root)
    for index in range(len(patternfiles)):
        file = patternfiles[index];
        filepath = pattern_root+"\\"+file[0:1].upper()+file[1:len(file)].lower()
        # os.rename(pattern_root+"\\"+file,pattern_root+"\\"+file[0:1].upper()+file[1:len(file)].lower())
        print(u"pattern files: "+  file)
        if(file.endswith(".java")):
            try:
                print(pattern)
                fo = open(filepath ,"r+")
                lines = []
                for line in fo: # 内置的迭代器, 效率很高
                    lines.append(line)

                lines.insert(0, U'package '+pattern+';\n') # 在第二行插入
                s = U''.join(lines)
                print s
                fo.seek(0,0)
                fo.write(s)
            except IOError:
                print U"Error: 没有找到文件或读取文件失败"
            except UnicodeDecodeError:
                print U"UnicodeDecodeError: 没有找到文件或读取文件失败"
            else:
                print U"内容写入文件成功"
            finally:
                fo.close()

