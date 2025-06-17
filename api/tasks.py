from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task
def send_registration_email(user_id):
    try:
        user = User.objects.get(id=user_id)
        subject = 'Welcome to Telegram_Bot!'
        message = f'Hi {user.username},\n\nThank you for registering with us!'
        from_email = 'noreply@telegrambot.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except User.DoesNotExist:
        pass
