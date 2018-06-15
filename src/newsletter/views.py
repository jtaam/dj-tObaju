from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from .models import NewsletterUser, Newsletter
from .forms import NewsletterUserSignUpForm, NewsletterCreationForm


def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Your Email Already Exists in our Database!',
                             'alert alert-warning alert-dismissible')
        else:
            instance.save()
            messages.success(request, 'Your Email subscribed successfully!', 'alert alert-success alert-dismissible')
            # Send Email
            subject = 'Thank your for joining our Newsletter'
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/templates/newsletters/sign_up_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletters/sign_up_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()

    context = {
        'form': form,
    }
    template = 'homepage/homepage.html'
    return render(request, template, context)
