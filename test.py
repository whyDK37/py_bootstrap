#!/usr/bin/python
# -*- coding: UTF-8 -*-

#将/dd 文件夹下的所有东西复制到/tmp
import json
import os,shutil,platform,sys
from collections import defaultdict

print (U"我是中文")
print (r'^time/plus/\d{1,2}/$');
maven_repo_root =   "D:\\mrp"
maven_onedrive_repo = "D:\\tmp1"

# shutil.copytree(maven_repo_root, maven_onedrive_repo)
os.popen("ipconfig ").read()
print(platform.system())

def tree(): return defaultdict(tree)

def dicts(t): return {k: dicts(t[k]) for k in t}

users = tree()
users['harold']['username'] = 'hrldcpr'
users['handler']['username'] = 'matthandlersux'

taxonomy = tree()
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Felidae']['Felis']['cat']
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Felidae']['Panthera']['lion']
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Canidae']['Canis']['dog']
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Canidae']['Canis']['coyote']
taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['tomato']
taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['potato']
taxonomy['Plantae']['Solanales']['Convolvulaceae']['Ipomoea']['sweet potato']

print(json.dumps(users))
print(dicts(taxonomy))