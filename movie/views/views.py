#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

from movie.models.movie import *

def index(request):
    return render_to_response("index.html")

def detail(request):
    return render_to_response("detail.html")

def list(request):
    return render_to_response("applist.html")
