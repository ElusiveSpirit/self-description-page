function toggleMessageForm() {
    $('div.contact div.message-block form').css('display', 'block');
    $('div.contact div.message-block div.message-success').css('display', 'none');
    $('div.contact div.info').animate({
        height: 'toggle'
    }, {
      queue:false,
    });
    $('div.contact div.message-block').animate({
        height: 'toggle'
    }, {
      queue:false,
    });
}


$('div.contact.container a.btn.open').add('div.contact.container a.btn-flat.close').click(function() {
    toggleMessageForm();
    $('#email').focus();
});

$('div.contact.container a.btn.send').click(function() {
    $('div.contact div.message-block form').animate({
        height: 'toggle'
    });
    $('div.contact div.message-block div.message-success').show();
    setTimeout(function() {
        if ($('div.contact div.message-block div.message-success').css('display') != 'none') {
            $('div.contact div.message-block div.message-success').css('display', 'none');
            toggleMessageForm();
        }
    }, 3000);
});
