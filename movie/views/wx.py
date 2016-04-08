#coding:utf-8
#########################################################################
# file: wx.py
# author: zhaowei
# mail: 30112737@qq.com
# created Time: 2016年04月08日 星期五 09时39分24秒
#########################################################################

from django.shortcuts import render
from django.shortcuts import render_to_response 
from movie.utils import utils
from movie.models.movie import *
from conf import *
from django.db.models import Q
from movie.models.movie import *
from django.http import HttpResponse
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.messages import *

wx_conf = WechatConf(
    token=WX_TOKEN,
    appid=WX_APPID,
    appsecret=WX_SECRET_KEY,
    encrypt_mode='safe',
    encoding_aes_key=WX_AES_KEY
)
wechat = WechatBasic(conf=wx_conf)

def CreateMenu(request):
    menu_data = {}

    all_btn = []
    first_btn = {}
    first_btn["type"] = "view"
    first_btn["name"] = u"更多电影资源..."
    first_btn["url"] = u"http://15dyy.com/wx_index/"
    all_btn.append(first_btn)

    menu_data["button"] = all_btn
    try:
        wechat.create_menu(menu_data)
    except Exception, e:
        return HttpResponse(u'create menu error.msg:%s' % str(e))
    return HttpResponse(u'create menu success!!!')
def WXInter(request):
    try:
        signature = request.GET['signature']
        timestamp = request.GET['timestamp']
        nonce = request.GET['nonce']
        #echostr = request.GET['echostr']
    except:
        return HttpResponse(u'get para error')
    msg_signature = ""
    try:
        msg_signature = request.GET['msg_signature']
    except:
        msg_signature = ""
    print "here"

    if not wechat.check_signature(signature, timestamp, nonce):
        print "check data error"
        return HttpResponse(u'check token error') 
    print "2here"
    post_data = request.body
    #parse datas
    try:
        wechat.parse_data(post_data,msg_signature=msg_signature, timestamp=timestamp, nonce=nonce)
    except Exception, e:
        print "error.msg:%s" % (str(e))
        return HttpResponse(u'parse_data error')
    print "return a message"

    if isinstance(wechat.message, TextMessage):
        content = wechat.message.content
        #回复一个图文信息
        articles = []
        onearticle = {}
        onearticle["title"] = u'查看"%s"相关电影' % content
        onearticle["description"] = u'查看"%s"相关电影' % content
        onearticle["url"] = u"http://15dyy.com/wx_search?keyword=%s" % content
        articles.append(onearticle)
        xml = wechat.response_news(articles)
        return HttpResponse(xml)
    if  isinstance(wechat.message, EventMessage):
        if wechat.message.type == "subscribe":
            articles = []
            onearticle = {}
            onearticle["title"] = u'欢迎关注，获取电影资源'
            onearticle["description"] = u'欢迎关注，获取电影资源'
            onearticle["url"] = u"http://15dyy.com/wx_index"
            articles.append(onearticle)
            xml = wechat.response_news(articles)
            return HttpResponse(xml)
    articles = []
    onearticle = {}
    onearticle["title"] = u'不能识别,点击获取更多电影资源'
    onearticle["description"] = u'不能识别，点击获取更多电影资源'
    onearticle["url"] = u"http://15dyy.com/wx_index"
    articles.append(onearticle)
    xml = wechat.response_news(articles)
    return HttpResponse(xml)

    #else:
        #return HttpResponse(echostr) #for the first time
