<!DOCTYPE html>
<html style="height:100%">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
        <title>wxtest</title>
        <link rel="stylesheet" href="/static/outlib/dist/lib/weui.css">
        <link rel="stylesheet" href="/static/outlib/dist/css/jquery-weui.css">
        <link rel="stylesheet" href="/static/css/wx_style.css">
    </head>

    <body style="height:100%">
        <div class="weui_tab">
          <div class="weui_tab_bd">
            <div class="weui_search_bar" id="search_bar">
              <form class="weui_search_outer" action="/wx_search">
                <div class="weui_search_inner">
                  <i class="weui_icon_search"></i>
                  <input type="search" name="keyword" class="weui_search_input" id="search_input" placeholder="搜索" required/>
                  <a href="javascript:search()"  class="weui_icon_clear" id="search_clear"></a>
                </div>
                <label for="search_input" class="weui_search_text" id="search_text">
                  <i class="weui_icon_search"></i>
                  <span>搜索</span>
                </label>
              </form>
              <a href="javascript:cancle()"  class="weui_search_cancel" id="search_cancel">取消</a>
            </div>

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

            
          <!--蠎暮Κ蟇ｼ闊ｪ譬?-->
          <div class="weui_tabbar">
            <a href="/wx_index" class="weui_tabbar_item ">
              <p class="weui_tabbar_label">最热应用</p>
            </a>
            <a href="javascript:;" class="weui_tabbar_item weui_bar_item_on">
              <p class="weui_tabbar_label">分类</p>
            </a>
            <a href="javascript:;" class="weui_tabbar_item">
              <p class="weui_tabbar_label">本周推荐</p>
            </a>
          </div>
        </div> 

        <script src="/static/outlib/dist/lib/jquery-2.1.4.js"></script>
        <script src="/static/outlib/dist/js/jquery-weui.js"></script>
        <script src="/static/js/wx.js"></script>
    </body>
</html>
