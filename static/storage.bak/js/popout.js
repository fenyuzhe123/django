
function show_popout(id){	
$(id).show();
$('#popout_bg').show();
$('#popout_box').show();
$('#popout_close').show();
$('#popout_btn').show();
reset_popout_content();
reset_popout_position();
}

function set_popout_box_W(){
 if($('#popout_box').length ==0){
        return false;
var popout_content_W=550;
    }


	$('.popout_box').css({width:popout_content_W});
}

function reset_popout_content(){
	popout_content_H = $('.popout_content').height();
	popout_content_W = $('.popout_content').width()+17;
	if( popout_content_H < 550)
   {
	$('.popout_content').css({'overflow':'auto'});
   }
   else {
	$('.popout_content').css({'width':popout_content_W,'height':'500px','overflow':'scroll','overflow-x':'hidden'});
	  };
	}

function reset_popout_position(){

	set_popout_box_W();
	$('#popout_bg').height(document.body.scrollHeight);
	box_halfH =  $('#popout_box').outerHeight()/2;
	box_halfW =  $('#popout_box').outerWidth()/2;
	if( document.documentElement.clientWidth < $('#popout_box').outerWidth() ){
		$('#popout_box').css({'left':'0'});
	}
	else{
		$('#popout_box').css({left: (document.documentElement.scrollLeft + document.body.scrollLeft + document.documentElement.clientWidth/2-box_halfW)});
	}
	if( document.documentElement.clientHeight < $('#popout_box').outerHeight() ){
		$('#popout_box').css({'top':'0'});
	}
	else{
		$('#popout_box').css({top: (document.documentElement.scrollTop + document.body.scrollTop + document.documentElement.clientHeight/2-box_halfH)});
	}
	}

	  
window.onscroll = function (){
	reset_popout_position();
  }
  
window.onresize = function (){
	reset_popout_position();

if(typeof scrollDivList!="undefined"){
for(var i=0; i<scrollDivList.length; i++) {
	scrollResetSize(scrollDivList[i]);
	}

}

	
  }
 $(document).ready(function() {
$('#popout_close').click(function(){
	  $('#popout_bg').hide();
	  $('#popout_box').hide();
	  $('#popout_box').children().hide();
	  });
	  });
 function detail(id){
            $('#edit_display').show();
            show_popout();
			  $.ajax({
                url: "get_info.php",
                type: 'POST',
                data: 'ty=detail&id=' + id,
                dataType: 'json',
                cache: false,
                success: function(json) {         				
                        $('#policyName').html(json.policy_name);
						$('#type').html(json.type);
						$('#product').html(json.product);
						$('#market').html(json.market);
					    $('#isReplicated').html(json.is_replicated);
						$('#site').html(json.site);
						$('#organization').html(json.organization);
						$('#detail_owner').html(json.owner);
						$('#detail_backup_client').html(json.backup_client);
						$('#scheduleType').html(json.schedule_type);
						$('#backupSelection').html(json.backup_selection);                         
                }
            });
          
        }
    