from django import forms
from django.core.mail import send_mail

from portfolio.settings import EMAIL_HOST_USER

from .models import Message, Profile


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['email', 'text']
        error_messages = {
            'email': {
                'required': "Необходимо ввести email",
                'invalid': "Введите корректный email",
            },
            'text': {
                'required': "Необходимо ввести текст",
            },
        }

    def save(self):
        msg = super(MessageForm, self).save()

        profile = Profile.objects.first()
        if profile and profile.send_email_messages:
            send_mail(
                'Mail from %s' % msg.email,
                'Mail from %s\n\nText:\n %s' % (msg.email, msg.text),
                EMAIL_HOST_USER,
                [profile.email],
                fail_silently=False,
            )

        return msg
