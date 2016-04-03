#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from movie.utils import utils
from movie.models.movie import *
from conf import *
from django.db.models import Q

# Create your views here.

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

def list(request):
    if request.method == 'POST':
        return render_to_response("error.html", {'msg':u'请求方式不正确'})
    page = 1
    type = "all"
    score = 0;
    if "type" in request.GET and request.GET["type"]:
        type = request.GET['type']
    if 'page' in request.GET and request.GET["page"]:
        page = int(request.GET['page'])
    if "score" in request.GET and request.GET["score"]:
        score = int(request.GET['score'])
    if score < 0 or score >= 10:
        return render_to_response("error.html",{"msg":u'评分数错误'})
    if page < 0:
        return render_to_response("error.html",{"msg":u'页码不正确'})
    fromindex = (page - 1)*PAGENUM
    endindex = page*PAGENUM
    print "fromindex:%d endindex:%d" % ( fromindex, endindex)
    pageallcount = 0
    if type == "all" and score == 0:
        search_data = moviedetail.objects.order_by("-createtime")[fromindex:endindex]
        pageallcount = moviedetail.objects.all().count()
    elif type == "all" and score != 0 :
        search_data = moviedetail.objects.filter(doubanscore_float__gte=score).order_by("-doubanscore_float")[fromindex:endindex]
        pageallcount = moviedetail.objects.filter(doubanscore_float__gte=score).count()
    else:
        search_data = moviedetail.objects.filter(type__contains=type).filter(doubanscore_float__gte=score).order_by("-doubanscore_float")[fromindex:endindex]
        pageallcount = moviedetail.objects.filter(type__contains=type).filter(doubanscore_float__gte=score).count()


    pagenums = utils.getpagenum(pageallcount,PAGENUM,page, 5)

    return render_to_response("applist.html",{'pagedata':moviedetail2dictlist(search_data, True),'pagenums':pagenums, 'score':score, 'type':type})

def wx_mv_list(request):
    render_dict = {}
    if request.method == 'POST':
        return render_to_response("error.html",{'msg':u'请求方式不正确'})
    type = None
    page = 1
    if "type" in request.GET and request.GET["type"]:
        type = request.GET['type']
    if "page" in request.GET and request.GET["page"]:
        page = int(request.GET["page"])
    if page < 0:
        return render_to_response("error.html", {"msg":u'页码不正确'})
    fromindex = (page - 1)*PAGENUM
    endindex = page*PAGENUM
    pageallcount = 0
    if not type or type == "all":
        search_data = moviedetail.objects.order_by("-createtime")[fromindex:endindex]
        pageallcount = moviedetail.objects.all().count()
    else:
        search_data = moviedetail.objects.filter(type__contains=type).order_by("-doubanscore_float")[fromindex:endindex]
        pageallcount = moviedetail.objects.filter(type__contains=type).order_by("-doubanscore_float").count()
    datalist = moviedetail2dictlist(search_data, False)

    print "all number is:%d" % len(datalist)
    IsFirstPage = False
    IsLastPage = False
    if page == 1:
        IsFirstPage = True
    if page >= pageallcount:
        IsLastPage = True
    render_dict["IsFirstPage"] = IsFirstPage
    render_dict["IsLastPage"] = IsLastPage
    render_dict["newlist"] = datalist
    render_dict["curpage"] = page
    render_dict["beforpage"] = page - 1
    render_dict["lastpage"] = page + 1
    urlpre = "/wx_mv_list?"
    if type:
        urlpre = urlpre + "type=%s" % type
    else:
        urlpre = urlpre + "type=all"
    beforurl = urlpre + "&page=%d" % (page - 1)
    lasturl = urlpre + "&page=%d" % (page + 1)

    render_dict["type"] = type
    render_dict["typemore"] = TYPEMORE
    render_dict["beforurl"] = beforurl
    render_dict["lasturl"] = lasturl
    #如果选择了类型，那么结果就按照分数来排序
    return render_to_response("wx_mv_list.tpl", render_dict)
def wx_search_ad(request):
    if request.method == 'POST':
        return render_to_response("error.html",{'msg':u'请求方式不正确'})
    type = None
    score = None
    page = 1
    if 'type' in request.GET and request.GET["type"]:
        type = request.GET['type']
    if 'score' in request.GET and request.GET['score']:
        score = request.GET['score']
    if 'page' in request.GET and request.GET["page"]:
        page = int(request.GET["page"])
    if type == None and score == None:
        return render_to_response("error.html",{"msg":u'参数不正确'})
    fromindex = (page - 1)*PAGENUM
    endindex = page*PAGENUM
    render_dict = {}
    if not type:
        search_data = moviedetail.objects.order_by("doubanscore_float")[fromindex:endindex+1]
    if not score:
        search_data = moviedetail.objects.filter(type__contains=type)[fromindex:endindex+1]
    if type and score:
        search_data = moviedetail.objects.filter(type__contains=type).order_by("doubanscore_float")[fromindex:endindex+1]
    datalist = moviedetail2dictlist(search_data, False)

def wx_search(request):
    if request.method == 'POST':
        return render_to_response("error.html",{'msg':u'请求方式不正确'})
    if 'keyword' in request.GET and request.GET['keyword']:
        keyword = request.GET["keyword"]
    else:
        return render_to_response("error.html",{"msg":u'参数不正确:-1'})
    render_dict = {}
    search_data = moviedetail.objects.filter(Q(title__contains=keyword)|Q(directors__contains=keyword)|Q(actors__contains=keyword))
    datalist = []
    for onedata in search_data:
        tmpone = {}
        tmpone["title"] = onedata.title
        tmpone["id"] = onedata.id
        tmpone["picurl"] = getpicurl(onedata.titlepic, False)
        tmpone["desc"] = convertlongtext(onedata.summary)
        datalist.append(tmpone)
    render_dict["newlist"] = datalist
    render_dict["keyword"] = keyword
    render_dict["count"] = len(datalist)
    return render_to_response("wx_search.tpl", render_dict)
def wx_index(request):
    #得到最热榜
    render_dict = {}
    hotlist = []
    hotsdata = moviehot.objects.all()
    for onehot in hotsdata:
        tmphot = {}
        tmphot["title"] = onehot.title
        tmphot["id"] = onehot.movie.id
        tmphot["picurl"] = getpicurl(onehot.movie.titlepic,False)
        hotlist.append(tmphot)
    if len(hotlist) >= 6:
        hotlist = hotlist[:6]
    render_dict["hotlist"] = hotlist

    #得到最新
    newdata = moviedetail.objects.order_by("-createtime")[:16]
    newlist = moviedetail2dictlist(newdata, False)
    render_dict["newlist"] = newlist

    return render_to_response("wx_index.tpl", render_dict)
def index(request):

    #得到大条幅
    topsdata = movietop.objects.all()
    render_dict = {}
    toplist = []
    for onetop in topsdata:
        tmptop = {} 
        tmptop["title"] = onetop.title
        tmptop["desc"] = onetop.desc
        tmptop["picurl"] = onetop.picurl
        tmptop["movieurl"] = onetop.movieurl
        toplist.append(tmptop)
    render_dict["toplist"] = toplist

    #得到最热榜
    hotlist = []
    hotsdata = moviehot.objects.all()
    for onehot in hotsdata:
        tmphot = {}
        tmphot["title"] = onehot.title
        tmphot["id"] = onehot.movie.id
        tmphot["picurl"] = getpicurl(onehot.movie.titlepic, True)
        hotlist.append(tmphot)
    if len(hotlist) >= 6:
        hotlist = hotlist[:6]
    render_dict["hotlist"] = hotlist

    #得到最新
    newdata = moviedetail.objects.order_by("-createtime")[:15]
    newlist = moviedetail2dictlist(newdata, True)
    render_dict["newlist"] = newlist
    
    return render_to_response("index.html", render_dict)

def moviedetail2dictlist(detaillist, isbig):
    afterlist = []
    for onemovie in detaillist:
        afterlist.append(moviedetail2dict(onemovie,isbig)) 
    return afterlist
def moviedetail2dict(detail,isbig):
    moviedict = {}
    moviedict["id"] = detail.id
    moviedict["title"] = detail.title
    moviedict["converttitle"] = converttitle(detail.title)
    moviedict["totle_title"] = detail.totle_title
    moviedict["picurl"] = getpicurl(detail.titlepic,isbig)
    moviedict["directors"] = detail.directors.replace('_',' ')
    moviedict["bianjus"] = detail.bianjus.replace('_',' ')
    moviedict["actors"] = detail.type.replace('_',' ')
    moviedict["types"] = detail.type.replace("_"," ")
    moviedict["country"] = detail.country.replace("_", " ")
    moviedict["uptime"] = detail.uptime
    moviedict["timelen"] = detail.timelen
    moviedict["altername"] = detail.altername
    moviedict["doubanscore"] = detail.doubanscore
    moviedict["summary"] = detail.summary
    moviedict["baiduyunlink"] = detail.baiduyunlink
    moviedict["baiduyunpwd"] = detail.baiduyunpwd
    print "mag_list [%s]" % detail.magnetlist
    moviedict["mag_list"] = detail.magnetlist.split("_")
    if  len(moviedict["mag_list"]) == 1  and moviedict["mag_list"][0] == "":
        moviedict["mag_list"] = None
    return moviedict

def wx_detail(request):
    if request.method == 'POST':
        return render_to_response("error.html",{'msg':u'请求方式不正确'})
    if 'id' in request.GET and request.GET['id']:
        movieid = request.GET["id"]
    else:
        return render_to_response("error.html",{"msg":u'参数不正确:-1'})
    try:
        moviedata = moviedetail.objects.get(id=movieid)
    except:
        return render_to_response("error.html",{"msg":u"您查找的数据不存在"})

    #构造数据
    moviedict = moviedetail2dict(moviedata, True)
    return render_to_response("wx_detail.tpl",moviedict)

def detail(request):
    if request.method == 'POST':
        return render_to_response("error.html",{'msg':u'请求方式不正确'})
    if 'id' in request.GET and request.GET['id']:
        movieid = request.GET["id"]
    else:
        return render_to_response("error.html", {'msg':u'参数不正确:-1'})
    try:
        moviedata = moviedetail.objects.get(id=movieid)
    except:
        return render_to_response("error.html",{'msg':u'您查找的数据不存在'})

    #构造数据
    moviedict = moviedetail2dict(moviedata, True)
    return render_to_response("detail.html",moviedict)

def addmovie(request):
    if request.method == 'GET':
        return render_to_response("error.html",{'msg':u'请求方式不正确'})
    ret,fieldval = RequestPostPa(request, "title")
    if not ret:
        return ReturnMsg("error.html", u"not found title")

def addindex(request):
    if not request.user.is_authenticated():
        return render_to_response("error.html", {'msg':u'暂无权限'})
    if request.method == 'POST':
        return render_to_response("error.html",{'msg':u'请求方式不正确'})
    return render_to_response("addindex.html")
