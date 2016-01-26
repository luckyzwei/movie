#!coding=utf-8
from django.db import models
'''
# Create your models here.
class director(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    class Meta:
        db_table = u'director'
        app_label = 'movie'
    def __unicode__(self):
        return u'%s' % name

class bianju(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    class Meta:
        db_table = u'bianju'
        app_label = 'movie'
    def __unicode__(self):
        return u'%s' % name

class actor(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    class Meta:
        db_table = u'actor'
        app_label = 'movie'
    def __unicode__(self):
        return u'%s' % name

class types(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    class Meta:
        db_table = u'types'
        app_label = 'movie'
    def __unicode__(self):
        return u'%s' % name

class country(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    class Meta:
        db_table = u'country'
        app_label = u'movie'
    def __unicode__(self):
        return u'%s' % name
'''

#大的幻灯片推荐
class movietop(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    desc = models.CharField(max_length=200, blank=False, null=False)
    picurl = models.CharField(max_length=500, blank=False, null=False)
    movieurl = models.CharField(max_length=500, blank=False, null=False)
    class Meta:
        db_table = u'top'
        app_label = 'movie'
    def __unicode__(self):
        return u"%s" % title
class moviedetail(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    totle_title = models.CharField(max_length=200, blank=False, null=False)
    directors = models.CharField(max_length=200, blank=False, null=False)
    bianjus = models.CharField(max_length=200, blank=False, null=False)
    actors = models.CharField(max_length=200, blank=False, null=False)
    type = models.CharField(max_length=200, blank=False, null=False)
    country = models.CharField(max_length=200, blank=False, null=False)
    #directors = models.ManyToManyField(director)
    #bianjus = models.ManyToManyField(bianju)
    #actors = models.ManyToManyField(actor)
    #types = models.ManyToManyField(types)
    #countrys = models.ManyToManyField(country)
    titlepic = models.CharField(max_length=200)
    qingxi = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    uptime = models.CharField(max_length=200)
    timelen = models.CharField(max_length=200)
    altername = models.CharField(max_length=200)
    doubanscore = models.CharField(max_length=200)

    summary = models.TextField()
    piclist = models.CharField(max_length=500) #使用下划线分割
    baiduyunlink = models.CharField(max_length=200)
    baiduyunpwd = models.CharField(max_length=50)
    magnetlist = models.CharField(max_length=500) #使用下划线分割
    class Meta:
        db_table = u'detail'
        app_label = 'movie'
    def __unicode__(self):
        return u'%s' % title

#热门推荐
class moviehot(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    movie = models.ForeignKey(moviedetail)
    class Meta:
        db_table = u'hot'
        app_label = 'movie'
