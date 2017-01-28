$.fn.smartFloat = function() {
	var position = function(element) {
		var top = element.position().top, pos = element.css("position");
		$(window).scroll(function() {
			var scrolls = $(this).scrollTop();
			if (scrolls > top) {
				if (window.XMLHttpRequest) {
					element.css({
						visibility:"visible",
						position: "fixed",
						top: 0,
						
					});	
				} else {
					element.css({
						visibility:"inherit",
						top: scrolls,
					});	
				}
			}else {
				element.css({
					visibility:"inherit",
					position: pos,
					top: top
				});	
			}
		});
};
	return $(this).each(function() {
		position($(this));						 
	});
};
$("#nav").smartFloat();
$("#month_box_div").smartFloat();
$("#homepage_hero_title").smartFloat();