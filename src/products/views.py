from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template

from django.shortcuts import render, get_object_or_404
from .models import Brand, ProductCategory, Colours, Product, CategoryGroup, ProductShareLinks
from shophome.models import TopOffer, Logo, ContactUsPage, StayInTouch

from newsletter.models import Newsletter, NewsletterUser
from newsletter.forms import NewsletterUserSignUpForm


def subscription_mail(tkeyword):
    form = NewsletterUserSignUpForm(tkeyword.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(tkeyword, 'Your Email Already Exists in our Database!',
                             'alert alert-warning alert-dismissible')
        else:
            instance.save()
            messages.success(tkeyword, 'Your Email subscribed successfully!', 'alert alert-success alert-dismissible')
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


def products_list(request):
    stayintouch = get_object_or_404(StayInTouch)
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    brands = Brand.objects.filter(status='published')
    categories = ProductCategory.objects.filter(status='published')
    colours = Colours.objects.all()
    products = Product.objects.filter(status='published')

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

    template = 'products/products_list.html'
    context = {
        'stayintouch': stayintouch,
        'offer': offer,
        'products': products,
        'categories': categories,
        'colours': colours,
        'brands': brands,
        'logo': logo,
        'contactus': contactus,
        'form': form,
    }
    return render(request, template, context)


def product_detail(request, pid):
    stayintouch = get_object_or_404(StayInTouch)
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    categories = ProductCategory.objects.filter(status='published')
    brands = Brand.objects.filter(status='published')
    product = get_object_or_404(Product, id=pid)
    products = Product.objects.filter(status='published')[0:3]
    recently_products = Product.objects.filter(status='published')[2:5]
    colours = Colours.objects.all()
    share_links = ProductShareLinks.objects.all()

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

    template = 'products/product_detail.html'
    context = {
        'stayintouch': stayintouch,
        'offer': offer,
        'product': product,
        'brands': brands,
        'colours': colours,
        'categories': categories,
        'products': products,
        'recently_products': recently_products,
        'logo': logo,
        'share_links': share_links,
        'contactus': contactus,
        'form': form,
    }
    return render(request, template, context)


def products_list_by_category(request, category):
    stayintouch = get_object_or_404(StayInTouch)
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    brands = Brand.objects.filter(status='published')
    categories = ProductCategory.objects.filter(status='published')
    colours = Colours.objects.all()
    products = Product.objects.filter(category=category)

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

    template = 'products/products_list.html'
    context = {
        'stayintouch': stayintouch,
        'offer': offer,
        'products': products,
        'categories': categories,
        'colours': colours,
        'brands': brands,
        'logo': logo,
        'contactus': contactus,
        'form': form,
    }
    return render(request, template, context)


def brands_list(request):
    stayintouch = get_object_or_404(StayInTouch)
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
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

    template = 'products/brand/brands_list.html'
    context = {
        'stayintouch': stayintouch,
        'brands': brands,
        'logo': logo,
        'contactus': contactus,
        'form': form,
    }
    return render(request, template, context)


def brand_detail(request, slug):
    stayintouch = get_object_or_404(StayInTouch)
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    brand = get_object_or_404(Brand, slug=slug)

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

    template = 'products/brand/brand_detail.html'
    context = {
        'stayintouch': stayintouch,
        'brand': brand,
        'logo': logo,
        'contactus': contactus,
        'form': form,
    }
    return render(request, template, context)
