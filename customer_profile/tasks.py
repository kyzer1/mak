from django.core.mail import send_mail


from celery import shared_task


@shared_task(name="send_mail")
def send_email_task(subject, message, email_from, recipient_list):
    send_mail(subject, message, email_from, recipient_list)
    return "email sended"