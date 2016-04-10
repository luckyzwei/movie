<!DOCTYPE html>
<html style="height:100%">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
        <title>51电影</title>
        <link rel="stylesheet" href="/static/outlib/dist/lib/weui.css">
        <link rel="stylesheet" href="/static/outlib/dist/css/jquery-weui.css">
        <link rel="stylesheet" href="/static/css/wx_style.css">
    </head>

    <body style="height:100%">

        <div class="weui_tab">
          <div class="weui_tab_bd">
        {% include 'wx_header.html' %}
          <!--最热应用-->
          <div class="weui-row"> 
            <span class="title">最热电影</span>
          </div>
          <div class="weui-row left-pa">
            {% for hotinfo in hotlist %}
                <div class="weui-col-33">
                    <article class="wx-block">
                        <a class="wx-block-thumbnail" href="/wx_detail?id={{hotinfo.id}}">
                            <img src="{{hotinfo.picurl}}" style="height:140px">
                        </a>
                        <div class="wx-block-contents">
                            <p class="wx-name">{{hotinfo.title}}<span class="label label-info">{{hotinfo.doubanscore}}</span></p>
                        </div>
                    </article>
                </div>
            {% endfor %}
          </div>
          <div class="weui-row">
            <span class="title">最新电影</span>
          </div>
          <div class="weui-row left-pa">
            {% for onenew in newlist %}
                <div class="weui-col-33">
                    <article class="wx-block">
                        <a class="wx-block-thumbnail" href="/wx_detail?id={{onenew.id}}">
                            <img src="{{onenew.picurl}}" style="height:140px">
                        </a>
                        <div class="wx-block-contents">
                            <p class="wx-name">{{onenew.converttitle}}<span class="label label-info">{{onenew.doubanscore}}分</span></p>
                        </div>
                    </article>
                </div>
            {% endfor %}
          </div>
          <div class="weui-row left-pa">
              <a href="/wx_mv_list" class="weui_btn weui_btn_mini weui_btn_primary">查看更多电影</a>
          </div>
          </div>

          {% include 'wx_foot.tpl' %}
        </div> 

        <script src="/static/outlib/dist/lib/jquery-2.1.4.js"></script>
        <script src="/static/outlib/dist/js/jquery-weui.js"></script>
        <script src="/static/js/wx.js"></script>
    </body>
</html>
