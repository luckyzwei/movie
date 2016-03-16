<!DOCTYPE html>
<html style="height:100%">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
        <title>weixintest</title>
        <link rel="stylesheet" href="/static/outlib/dist/lib/weui.css">
        <link rel="stylesheet" href="/static/outlib/dist/css/jquery-weui.css">
        <link rel="stylesheet" href="/static/css/wx_style.css">
    </head>

    <body style="height:100%">

        <div class="weui_tab">
          <div class="weui_tab_bd">
            <div class="weui_search_bar" id="search_bar">
              <form class="weui_search_outer">
                <div class="weui_search_inner">
                  <i class="weui_icon_search"></i>
                  <input type="search" class="weui_search_input" id="search_input" placeholder="搜索" required/>
                  <a href="javascript:" class="weui_icon_clear" id="search_clear"></a>
                </div>
                <label for="search_input" class="weui_search_text" id="search_text">
                  <i class="weui_icon_search"></i>
                  <span>搜索</span>
                </label>
              </form>
              <a href="javascript:" class="weui_search_cancel" id="search_cancel">取消</a>
            </div>

          <!--最热应用-->
          <div class="weui-row"> 
            <span class="title">最热应用</span>
            <hr/>
          </div>
          <div class="weui-row left-pa">
            {% for hotinfo in hotlist %}
                <div class="weui-col-50">
                    <article class="wx-block">
                        <a class="wx-block-thumbnail" href="/wx_detail?id={{hotinfo.id}}">
                            <img src="{{hotinfo.picurl}}" style="height:300px">
                        </a>
                        <div class="wx-block-contents">
                            <p class="wx-name">{{hotinfo.title}}<span class="label label-info">{{10}}分</span></p>
                        </div>
                    </article>
                </div>
            {% endfor %}
          </div>
          </div>

          <div class="weui-row">
            <span class="title">最新应用</span>
            <hr/>
          </div>
          <div class="weui-row left-pa">
            {% for onenew in newlist %}
                <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12">
                    <article class="wx-block">
                        <a class="wx-block-thumbnail" href="/wx_detail?id={{onenew.id}}">
                            <img src="{{onenew.picurl}}" style="height:300px">
                        </a>
                        <div class="wx-block-contents">
                            <p class="wx-name">{{onenew.title}}<span class="label label-info">{{10}}分</span></p>
                        </div>
                    </article>
                </div>
            {% endfor %}
          </div>
            
          <!--蠎暮Κ蟇ｼ闊ｪ譬?-->
          <div class="weui_tabbar">
            <a href="javascript:;" class="weui_tabbar_item weui_bar_item_on">
             <div class="weui_tabbar_icon">
                <img src="path/to/images/icon_nav_button.png" alt="">
              </div>
              <p class="weui_tabbar_label">最热应用</p>
            </a>
            <a href="javascript:;" class="weui_tabbar_item">
              <div class="weui_tabbar_icon">
                <img src="path/to/images/icon_nav_msg.png" alt="">
              </div>
              <p class="weui_tabbar_label">分类</p>
            </a>
            <a href="javascript:;" class="weui_tabbar_item">
              <div class="weui_tabbar_icon">
                <img src="path/to/images/icon_nav_article.png" alt="">
              </div>
              <p class="weui_tabbar_label">本周推荐</p>
            </a>
          </div>
        </div> 

        <script src="/static/outlib/dist/lib/jquery-2.1.4.js"></script>
        <script src="/static/outlib/dist/js/jquery-weui.js"></script>
    </body>
</html>