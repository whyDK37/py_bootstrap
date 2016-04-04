#!/usr/bin/python
# -*- coding: UTF-8 -*-
import support, os, sys,random, json.tool

obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj)
print(sys.argv)
print(os.getcwd())
print(random.choice(['apple', 'pear', 'banana']))
support.print_func("Zara")

print( os.path.expanduser('~'))
userhome = os.path.expanduser('~')
print(userhome+"\\.gradle\\caches\\modules-2\\files-2.1")

print(os.listdir(userhome+"/.gradle"));