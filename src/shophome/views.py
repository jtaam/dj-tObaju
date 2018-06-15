from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template

from django.shortcuts import render, get_object_or_404
from .models import TopSlider, Advantages, GetInspired, TopOffer, Logo, Faq, ContactUsPage, AboutUs, StayInTouch
from products.models import Product, Colours, ProductCategory, Brand
from blog.models import Post

from newsletter.models import Newsletter, NewsletterUser
from newsletter.forms import NewsletterUserSignUpForm


def homepage(request):
    stayintouch = get_object_or_404(StayInTouch)
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    categories= ProductCategory.objects.filter(status='published')
    sliders = TopSlider.objects.filter(status='published')
    advantages = Advantages.objects.filter(status='published')
    products = Product.objects.filter(status='published')
    get_inspired_images = GetInspired.objects.filter(status='published')
    posts = Post.objects.filter(status='published')[0:2]

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

    template = 'homepage/homepage.html'
    context = {
        'stayintouch': stayintouch,
        'logo': logo,
        'offer': offer,
        'sliders': sliders,
        'advantages': advantages,
        'products': products,
        'inspires': get_inspired_images,
        'posts': posts,
        'title': 'home page',
        'contactus': contactus,
        'categories': categories,
        'form': form,
    }
    return render(request, template, context)


def faq(request):
    stayintouch = get_object_or_404(StayInTouch)
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
    faqs = Faq.objects.filter(status='published')
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    categories = ProductCategory.objects.filter(status='published')
    colours = Colours.objects.all()
    brands = Brand.objects.filter(status='published')

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

    template = 'pages/faq.html'
    context = {
        'stayintouch': stayintouch,
        'faqs': faqs,
        'logo': logo,
        'offer': offer,
        'categories': categories,
        'colours': colours,
        'brands': brands,
        'contactus': contactus,
        'categories': categories,
        'form': form,
    }
    return render(request, template, context)


def contact(request):
    stayintouch = get_object_or_404(StayInTouch)
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)

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

    template = 'contact/contact.html'
    context = {
        'stayintouch': stayintouch,
        'logo': logo,
        'offer': offer,
        'contactus': contactus,
        'categories': categories,
        'form': form,
    }
    return render(request, template, context)


def terms_and_conditions(request):
    stayintouch = get_object_or_404(StayInTouch)
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)

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

    template = 'pages/terms_and_conditions.html'
    context = {
        'stayintouch': stayintouch,
        'logo': logo,
        'offer': offer,
        'contactus': contactus,
        'categories': categories,
        'form': form,
    }
    return render(request, template, context)


def about_us(request):
    stayintouch = get_object_or_404(StayInTouch)
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
    about_us_data = get_object_or_404(AboutUs)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)

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

    template = 'pages/about_us.html'
    context = {
        'stayintouch': stayintouch,
        'logo': logo,
        'offer': offer,
        'about_us_data': about_us_data,
        'contactus': contactus,
        'categories': categories,
        'form': form,
    }
    return render(request, template, context)
