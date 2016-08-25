function toggleLoading() {
    $('div.loading-block a.btn').hide();
    $('div.loading-block div.preloader-wrapper').show();
}

$('div.loading-block a.btn').click(function() {
    toggleLoading();
    setTimeout(function() {
        $('div.loading-block div.preloader-wrapper').hide();
        $('div.loading-block span.result').show();
    }, 2000);
});
