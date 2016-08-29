function toggleMessageForm() {
    $('div.contact div.message-block div.preloader-wrapper').css('display', 'none');
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


$('#text').focus(function() {
    $(this).removeClass('invalid');
});


$('div.contact.container a.btn.send').click(function() {

    if ($('#email').val().length == 0) {
        $('#email').removeClass('valid');
        $('#email').addClass('invalid');
    }

    if ($('#text').val().length == 0) {
        $('#text').removeClass('valid');
        $('#text').addClass('invalid');
    }

    if ($('#text').hasClass('invalid') ||
            $('#email').hasClass('invalid')) {
        return;
    }
    var data = {
        'email': $('#email').val(),
        'text': $('#text').val(),
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
    };

    $('div.contact div.message-block form').animate({
        height: 'toggle'
    });
    $('div.contact div.message-block div.preloader-wrapper').show();
    $.ajax({
        type: 'POST',
        url: '/send_message/',
        data: data,
        success: function(data) {
          $('div.contact div.message-block div.preloader-wrapper').hide();
            if (data.status == 'ok') {
                $('div.contact div.message-block div.message-success').show();
                setTimeout(function() {
                    if ($('div.contact div.message-block div.message-success').css('display') != 'none') {
                        $('div.contact div.message-block div.message-success').css('display', 'none');
                        toggleMessageForm();
                    }
                }, 3000);
            } else if (data.code = 501) {
                $('div.contact div.message-block form').animate({
                    height: 'toggle'
                });
                errors = JSON.parse(data.errors);

                var error;
                if (errors.email) {
                    error = errors.email[0];
                    $('label[for="email"]').attr('data-error', error.message)
                    $('#email').removeClass('valid');
                    $('#email').addClass('invalid');
                }

                if (errors.text) {
                    error = errors.text[0];
                    $('label[for="text"]').attr('data-error', error.message)
                    $('#text').removeClass('valid');
                    $('#text').addClass('invalid');
                }
            }
        },
        error: function(e) {
        }
    });

});
