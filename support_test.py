#!/usr/bin/python

import support
import os
import sys,random
import json.tool

obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj)
print(sys.argv)
print(os.getcwd())
print(random.choice(['apple', 'pear', 'banana']))
support.print_func("Zara")