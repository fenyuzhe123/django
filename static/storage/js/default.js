login_halfH = $('#login').innerHeight()/2;
header_halfH =  $('#header').innerHeight()/2;
footer_halfH =  $('#footer').innerHeight()/2;
header_H =  $('#header').innerHeight();

function openwindow(url,name,iWidth,iHeight)
{
    var url; 
    var name;
    var iWidth; 
    var iHeight; 
    var iTop = (window.screen.availHeight-30-iHeight)/2;
    var iLeft = (window.screen.availWidth-10-iWidth)/2;
    window.open(url,name,'height='+iHeight+',,innerHeight='+iHeight+',width='+iWidth+',innerWidth='+iWidth+',top='+iTop+',left='+iLeft+',toolbar=no,menubar=no,scrollbars=auto,resizeable=no,location=no,status=no');
    logWindow.focus();
    return false;
}

function show_popout(){	
    $('#popout_bg').show();
    $('#popout_box').show();
    $('#popout_close').show();
    reset_popout_position();
}

function reset_popout_position(){
   if($('#popout_box').length ==0){
        return true;
    } 
    $('#popout_bg').height(document.body.scrollHeight);
    box_halfH =  $('#popout_box').outerHeight()/2;
    box_halfW =  $('#popout_box').outerWidth()/2;
    $('#popout_box').css({
        top: (document.documentElement.scrollTop + document.body.scrollTop + document.documentElement.clientHeight/2-box_halfH)
    });
    $('#popout_box').css({
        left: (document.documentElement.scrollLeft + document.body.scrollLeft + document.documentElement.clientWidth/2-box_halfW)
    });
}
	 
window.onload = function (){
    $('#login').css({
        top: (document.documentElement.scrollTop + document.body.scrollTop + document.documentElement.clientHeight/2-header_halfH-footer_halfH-login_halfH+header_H)
    });   
}

window.onscroll = function (){
    reset_popout_position();
    $('#login').css({
        top: (document.documentElement.scrollTop + document.body.scrollTop + document.documentElement.clientHeight/2-header_halfH-footer_halfH-login_halfH+header_H)
    });
}
  
window.onresize = function (){
    reset_popout_position();
    $('#login').css({
        top: (document.documentElement.scrollTop + document.body.scrollTop + document.documentElement.clientHeight/2-header_halfH-footer_halfH-login_halfH+header_H)
    });
}
  
$('#popout_close').click(function(){
    $('#popout_bg').hide();
    $('#popout_box').hide();
    $('#popout_box').children().hide();
});
