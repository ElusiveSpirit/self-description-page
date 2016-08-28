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


function copy_url() {
    var inp = document.getElementById('url_copy');

    // is element selectable?
    if (inp && inp.select) {
      // select text
        inp.select();

        try {
            // copy text
            document.execCommand('copy');
            inp.blur();
            Materialize.toast('Link has been copied', 3000)
        }
        catch (err) {
            alert('please press Ctrl/Cmd+C to copy');
        }
    }
}
