#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from movie.utils import utils
from movie.models.movie import *
from conf import *

# Create your views here.

from movie.models.movie import *

def index(request):
    return render_to_response("index.html")

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
    moviedict = {}
    moviedict["title"] = moviedata.title
    moviedict["totle_title"] = moviedata.totle_title
    moviedict["picurl"] = PICURLPRE + moviedata.titlepic.split('/')[-1]
    moviedict["directors"] = moviedata.directors.replace('_',' ')
    moviedict["bianjus"] = moviedata.bianjus.replace('_',' ')
    moviedict["actors"] = moviedata.actors.replace('_',' ')
    moviedict["types"] = moviedata.type.replace("_",' ')
    moviedict["country"] = moviedata.country.replace("_"," ")
    moviedict["uptime"] = moviedata.uptime
    moviedict["timelen"] = moviedata.timelen
    moviedict["altername"] = moviedata.altername
    moviedict["doubanscore"] = moviedata.doubanscore
    moviedict["summary"] = moviedata.summary
    moviedict["baiduyunlink"] = moviedata.baiduyunlink
    moviedict["baiduyunpwd"] = moviedata.baiduyunpwd
    moviedict["mag_list"] = moviedata.magnetlist.split("_")
    print moviedict["mag_list"]
    print "maglist:%s" % moviedata.magnetlist
    return render_to_response("detail.html",moviedict)

def list(request):
    return render_to_response("applist.html")
