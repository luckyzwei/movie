$(document).ready(function(){
    console.log("in here");
    $("11form").submit(function(e){
        var search_data  = $('#search_input').val();
        newurl = '/wx_search?keyword'+search_data;
        console.log("redirect to url:" + newurl);
        window.location.href1=newurl;
    });
});
