from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@shared_task
def send_welcome_email(email):
    """
    Task to send welcome email to customer on first signup
    """
    subject, from_email, to = "Welcome to APO-Store", "support@apostore.com", "email"

    context = {
        "name": to,
        "action_url": "https://apo-store.com/auth/login",
        "support_email": "support@apo-store.com",
        "live_chat_url": "chat@apo-store.com"
    }

    html_context = render_to_string("email_template.html", context)
    text_content = strip_tags(html_context)

    email = EmailMultiAlternatives(
        subject,
        text_content,
        from_email,
        [to]
    )

    email.attach_alternative(html_context, "text/html")
    email.send()
