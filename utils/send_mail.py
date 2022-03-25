from django.core.mail import EmailMessage

def send_mail(email, another_user):
    mail_subject = 'Вы понравились кое-кому!'
    message = f'Вы понравились {another_user.first_name}<br>Почта:{another_user.email}'
    msg = EmailMessage(mail_subject, message, to=[email])
    msg.content_subtype = 'html'
    msg.send()
