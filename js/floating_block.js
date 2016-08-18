var floating = $('main div.project-detail div.floating-block');
var floating_top = $(floating).css('top');

$(document).ready(function(){
    $(floating).css('top', $(floating).offset().top);
    $(floating).css('left', $(floating).offset().left);
    $(floating).css('position', 'fixed');
 });

$(window).resize(function() {
    $(floating).css('position', 'absolute');
    $(floating).css('top', floating_top);
    $(floating).css('left', '');

    $(floating).css('top', $(floating).offset().top);
    $(floating).css('left', $(floating).offset().left);
    $(floating).css('position', 'fixed');

})
