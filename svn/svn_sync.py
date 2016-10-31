#!/usr/bin/python
#coding=utf-8

import os
import commands
import sys
import logging

def init_log(log_level,logpath):
    logger = logging.getLogger()
    '''''
    from logging.handlers import RotatingFileHandler
    ro_hdlr=RotatingFileHandler(logpath, maxBytes=0,backupCount=5)
    logger.addHandler(ro_hdlr)
    ro_hdlr.doRollover()
    '''
    hdlr = logging.FileHandler(logpath,'a')
    formatter = logging.Formatter('%(asctime)s [%(levelname)-8s %(module)s:%(lineno)d] %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(log_level)

    return logger

log=init_log(0,'sync.log')

log.info(sys.argv[1])
repos=os.path.basename(sys.argv[1])
log.info("*"*20+repos)

# output=commands.getoutput('/usr/local/subversion/bin/svnsync sync --non-interactive --username admin --password admin123 svn://192.168.11.94/'+repos)
output=commands.getoutput('svnsync sync --non-interactive --username admin --password admin123 svn://192.168.11.94/'+repos)
log.info('sync log :'+output)