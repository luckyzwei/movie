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
