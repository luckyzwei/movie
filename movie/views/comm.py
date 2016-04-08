#coding:utf-8
#########################################################################
# file: comm.py
# author: zhaowei
# mail: 30112737@qq.com
# created Time: 2016年04月08日 星期五 10时13分31秒
#########################################################################

from django.shortcuts import render
from django.shortcuts import render_to_response 
from movie.utils import utils
from movie.models.movie import *
from conf import *
from django.db.models import Q
from movie.models.movie import *


def getpicurl(oldurl, isbig):
    if isbig:
        newurl = PICURLPRE + FILEPRE + oldurl.split('/')[-1]
        print "oldurl:%s newurl:%s" % (oldurl, newurl)
    else:
        newurl = MIN_PICURLPRE + MIN_FILEPRE + oldurl.split('/')[-1]
        print "oldurl:%s newurl:%s" % (oldurl, newurl)
    return newurl
def converttitle(title):
    if len(title) > 8:
        return u"%s.." % title[:4]
    return title
def convertlongtext(strnumber):
    if len(strnumber) > 10:
        return "%s..." % strnumber[:10]
    return strnumber
