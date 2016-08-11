#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
"""

import os,shutil

package = U"D:\\23\\"

patterns = os.listdir(package)
for index in range(len(patterns)):
    pattern = patterns[index];
    pattern_root = package+pattern
    print(u"pattern: "+  pattern_root)
    patternfiles = os.listdir(pattern_root)
    for index in range(len(patternfiles)):
        file = patternfiles[index];
        print(pattern_root+"\\"+file[0:1].upper()+file[1:len(file)].lower())
        # os.rename(pattern_root+"\\"+file,pattern_root+"\\"+file[0:1].upper()+file[1:len(file)].lower())
        print(u"pattern files: "+  file)
        if(file.endswith(".java")):
            pass
            break

        break

    break