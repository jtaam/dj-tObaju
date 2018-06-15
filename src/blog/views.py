from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from .models import Post
from shophome.models import TopOffer, Logo, ContactUsPage, StayInTouch
from products.models import ProductCategory
from newsletter.models import Newsletter, NewsletterUser
from newsletter.forms import NewsletterUserSignUpForm


def blog_list(request):
    stayintouch = get_object_or_404(StayInTouch)
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    posts = Post.objects.filter(status='published').order_by('-create')
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

    template = 'blog/blog_list.html'
    context = {
        'stayintouch': stayintouch,
        'offer': offer,
        'posts': posts,
        'logo': logo,
        'contactus': contactus,
        'categories': categories,
        'form': form,
    }
    return render(request, template, context)


def blog_detail(request, pid):
    stayintouch = get_object_or_404(StayInTouch)
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    post = get_object_or_404(Post, id=pid)
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
    template = 'blog/blog_detail.html'
    context = {
        'stayintouch': stayintouch,
        'offer': offer,
        'post': post,
        'logo': logo,
        'contactus': contactus,
        'categories': categories,
        'form': form,
    }
    return render(request, template, context)


