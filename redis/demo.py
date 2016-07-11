#!/usr/bin/env python
#-*- coding: utf-8 -*-
import redis

#这里替换为连接的实例host和port
host = '127.0.0.1'
port = 6379

#这里替换为实例id和实例password
user='username'
pwd='password'

#连接时通过password参数指定AUTH信息，由user,pwd通过":"拼接而成
# r = redis.StrictRedis(host=host, port=port, password=user+':'+pwd)
r = redis.StrictRedis(host=host, port=port)

#连接建立后就可以进行数据库操作，详情文档参考https://github.com/andymccurdy/redis-py
r.set('name', 'python_test');
print r.get('name')