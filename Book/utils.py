from django.conf import settings
from django.core.mail import send_mail

def send_burgain_notification(email, name, book, decision):
    try:
        subject = "Burgain Notification"
        message = f"Hello {name}, \nThe burgain you place on {book} has been {decision}"
        from_email = settings.SITE_EMAIL
        to_email = email
        send_mail(
            subject,
            message,
            from_email,
            [to_email,]
        )
    except Exception as e:
        raise e