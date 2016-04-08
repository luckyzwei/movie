<!DOCTYPE html>
<html style="height:100%">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
        <title>出错了-51电影</title>
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
                            <a href="javascript:" class="weui_icon_clear" id="search_clear"></a>
                        </div>
                        <label for="search_input" class="weui_search_text" id="search_text">
                            <i class="weui_icon_search"></i>
                            <span>搜索</span>
                        </label>
                    </form>
                    <a href="javascript:" class="weui_search_cancel" id="search_cancel">取消</a>
                </div>

                <div class="weui-row">
                    <span class="error_title">您要找的页面不存在</span>
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
              <p class="weui_tabbar_label">关于</p>
            </a>
          </div>
        </div>
        <script src="/static/outlib/dist/lib/jquery-2.1.4.js"></script>
        <script src="/static/outlib/dist/js/jquery-weui.js"></script>
        <script src="/static/js/wx.js"></script>
    </body>
</html>
