<!DOCTYPE html>
<html style="height:100%">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
        <title>电影列表-51电影</title>
        <link rel="stylesheet" href="/static/outlib/dist/lib/weui.css">
        <link rel="stylesheet" href="/static/outlib/dist/css/jquery-weui.css">
        <link rel="stylesheet" href="/static/css/wx_style.css">
    </head>

    <body style="height:100%">
        <div class="weui_tab">
          <div class="weui_tab_bd">

          {% include 'wx_header.tpl'%}
          <!--各种类型-->
          <div class="weui-row">
            <span class="title">类型</span>
          </div>
          <div class="weui-row typelist" id="short_types">
             <div class="weui-col-20">
                <a href="/wx_mv_list?type=all">全部</a>
             </div>
             <div class="weui-col-20">
                <a href="/wx_mv_list?type=传记">传记</a>
             </div>
             <div class="weui-col-20">
                <a href="/wx_mv_list?type=喜剧">喜剧</a>
             </div>
             <div class="weui-col-20">
                <a href="/wx_mv_list?type=剧情">剧情</a>
             </div>
             <div class="weui-col-20">
                <a href="/wx_mv_list?type=枪战">枪战</a>
             </div>
             <div class="weui-col-20">
                <a href="/wx_mv_list?type=恐怖">恐怖</a>
             </div>
             <div class="weui-col-20">
                <a href="/wx_mv_list?type=励志">励志</a>
             </div>
             <div class="weui-col-20">
                <a href="/wx_mv_list?type=动画">动画</a>
             </div>
             <div class="weui-col-20">
                <a href="/wx_mv_list?type=歌舞">歌舞</a>
             </div>
             <div class="weui-col-20">
                <a href="javascript:open()">更多..</a>
             </div>
          </div>
          <div class="weui-row typelist" style="display:none;" id="long_types">
            <div class="weui-row">
               <div class="weui-col-20">
                  <a href="/wx_mv_list?type=all">全部</a>
               </div>
               <div class="weui-col-20">
                  <a href="/wx_mv_list?type=传记">传记</a>
               </div>
               <div class="weui-col-20">
                  <a href="/wx_mv_list?type=喜剧">喜剧</a>
               </div>
               <div class="weui-col-20">
                  <a href="/wx_mv_list?type=剧情">剧情</a>
               </div>
               <div class="weui-col-20">
                  <a href="/wx_mv_list?type=枪战">枪战</a>
               </div>
               <div class="weui-col-20">
                  <a href="/wx_mv_list?type=恐怖">恐怖</a>
               </div>
               <div class="weui-col-20">
                  <a href="/wx_mv_list?type=励志">励志</a>
               </div>
               <div class="weui-col-20">
                  <a href="/wx_mv_list?type=动画">动画</a>
               </div>
               <div class="weui-col-20">
                  <a href="/wx_mv_list?type=歌舞">歌舞</a>
               </div>
            {% for onetype in typemore %}
                <div class="weui-col-20">
                    <a href="/wx_mv_list?type={{onetype}}">{{onetype}}</a>
                </div>
            {% endfor %}
            <div class="weui-col-20">
                  <a href="javascript:close()">收起</a>
            </div>
            </div>
          </div>

          <!--最新应用-->
          <div class="weui-row"> 
            <span class="title">最新应用</span>
            <hr/>
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

          <!--页码-->
          <div class="weui-row pageinfo">
            {% if IsFirstPage %}
            {% else %}
                <a href="{{beforurl}}">上一页</a>
            {% endif %}
            {% if IsLastPage %}
            {% else %}
                <a href="{{lasturl}}">下一页</a>
            {% endif %}
          </div>
          </div>

            {% include 'wx_header.tpl' %}
        </div> 

        <script src="/static/outlib/dist/lib/jquery-2.1.4.js"></script>
        <script src="/static/outlib/dist/js/jquery-weui.js"></script>
        <script src="/static/js/wx.js"></script>
    </body>
</html>
