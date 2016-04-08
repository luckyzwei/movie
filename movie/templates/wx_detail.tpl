<!DOCTYPE html>
<html style="height:100%">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
        <title>{{title}}-51电影</title>
        <link rel="stylesheet" href="/static/outlib/dist/lib/weui.css">
        <link rel="stylesheet" href="/static/outlib/dist/css/jquery-weui.css">
        <link rel="stylesheet" href="/static/css/wx_style.css">
        <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" />
    </head>

    <body style="height:100%">
        <div class="weui_tab">
            <div class="weui_tab_bd">
                <div class="weui_search_bar" id="search_bar">
                      <form class="weui_search_outer" action="/wx_search">
                        <div class="weui_search_inner">
                          <i class="weui_icon_search"></i>
                          <input type="search" name="keyword" class="weui_search_input" id="search_input" placeholder="搜索" required/>
                          <a href="javascript:" class="weui_icon_clear" id="search_clear"></a>
                        </div>
                        <label for="search_input" class="weui_search_text" id="search_text">
                          <i class="weui_icon_search"></i>
                          <span>搜索</span>
                        </label>
                      </form>
                      <a href="javascript:" class="weui_search_cancel" id="search_cancel">取消</a>
                </div>

                <div class="container-fluid detail_content">
                    <ol class="breadcrumb">
                        <li><a href="#">首页</a></li>
                        <li>{{title}}</li>
                    </ol>
                    <div class="row">
                        <div class="col-md-12"> 
                            <h1 class="wx-info-title">
                                {{totle_title}}
                                <span class="wx-info-year">{{year}}</span>
                            </h1>
                            <div class="row">
                                <div class="col-md-4" style="padding-right:5px;">
                                    <a href="#" style="display:block;position:relative;">
                                        <img class="wx-img-thumbnail" alt="pic" width="100%" src="{{picurl}}">
                                    </a>
                                </div>
                                <div class="col-md-8" style="padding-right:5px;">
                                    <table class="table table-striped table-condensed table-bordered" style="margin-bottom:10px; font-size:12px;">
                                        <tbody>
                                            <tr>
                                                <td class="wx-span2"><span class="info-label">导演</span></td>
                                                <td>{{directors}}</td>
                                            </tr>
                                            <tr>
                                                <td class="wx-span2"><span class="info-label">编剧</span></td>
                                                <td>{{bianjus}}</td>
                                            </tr>
                                            <tr>
                                                <td class="wx-span2"><span class="info-label">主演</span></td>
                                                <td id="casts" style="position:relative;">{{actors}}</td>
                                            </tr>
                                            <tr>
                                                <td class="wx-span2"><span class="info-label">类型</span></td>
                                                <td>{{types}}</td>
                                            </tr>
                                            <tr>
                                                <td class="wx-span2"><span class="info-label">制片国家</span></td>
                                                <td>{{country}}</td>
                                            </tr>
                                            <tr>
                                                <td class="wx-span2"><span class="info-label">上映时间</span></td>
                                                <td>{{timelen}}</td>
                                            </tr>
                                            <tr>
                                                <td class="wx-span2"><span class="info-label">又名</span></td>
                                                <td>{{altername}}</td>
                                            </tr>
                                            <tr>
                                                <td class="wx-span2"><span class="info-label">评分</span></td>
                                                <td>豆瓣:{{doubanscore}}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <p style="color:#777;"><strong>剧情介绍:</strong></p>
                                    <p class="summary">{{summary}}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-12">
                            <div class="panel panel-default download-list">
                                <div class="panel-heading">
                                    <strong>《{{title}}》百度网盘 迅雷下载</strong>
                                </div>
                                <table class="table" style="word-break:break-all; word-wrap:break-all;">
                                    <tbody>
                                        <tr>
                                            <td style="vertical-align:middle;padding-right:0;" align="center" width="50px"><span class="wx-baidu-icon">网盘</span></td>
                                            <td class="text-break">
                                                <div style="width:100%; height:20px; overflow:hidden;">
                                                    {%ifequal baiduyunlink ""%}
                                                    <span>暂无资源,点此添加</span>
                                                    {%else%}
                                                    <a rel="nofollow" target="_blank" href="{{baiduyunlink}}">{{title}}--百度网盘，密码:</a>
                                                    <strong>{{baiduyunpwd}}</strong>
                                                    {%endifequal%}
                                                </div>
                                            </td>
                                        </tr>
                                        {% for magnet in mag_list %}
                                        <tr>
                                            <td style="vertical-align:middle;padding-right:0" align="center" width="50px"><span>磁力</span></td>
                                            <td class="text-break">
                                                <div style="width:100%;">
                                                    <!--a rel="nofollow" target="_blank" href="{{magnet}}">{{magnet}}</a-->
                                                    <span>{{magnet}}</span>
                                                </div>
                                            </td>
                                        </tr>
                                        {% endfor %}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>




            </div>
          <div class="weui_tabbar">
            <a href="/wx_index" class="weui_tabbar_item">
              <p class="weui_tabbar_label">首页</p>
            </a>
            <a href="/wx_mv_index" class="weui_tabbar_item">
              <p class="weui_tabbar_label">分类</p>
            </a>
            <a href="javascript:;" class="weui_tabbar_item">
              <p class="weui_tabbar_label">关于</p>
            </a>
          </div>
        </div> 

        <script src="/static/outlib/dist/lib/jquery-2.1.4.js"></script>
        <script src="/static/outlib/dist/js/jquery-weui.js"></script>
        </div>
    </body>
</html>
