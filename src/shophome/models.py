from django.db import models


class Logo(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    image_large = models.ImageField(upload_to='homepage/logo/%Y/%m/%d/', null=True, blank=True)
    image_small = models.ImageField(upload_to='homepage/logo/%Y/%m/%d/', null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


class TopOffer(models.Model):
    percentage = models.CharField(max_length=2)
    limit = models.CharField(max_length=5)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.percentage


class TopSlider(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='homepage/top-slider/%Y/%m/%d/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, default='draft', max_length=20)

    class Meta:
        verbose_name = 'Top Slider'
        verbose_name_plural = 'Top Slider'

    def __str__(self):
        return self.name


class Advantages(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text='fa-hearts , ref: https://fontawesome.bootstrapcheatsheets.com/')
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'advantage'
        verbose_name_plural = 'advantages'


class GetInspired(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='homepage/get-inspired/%Y/%m/%d/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, default='draft', max_length=20)

    class Meta:
        verbose_name = 'Get Inspired Image'
        verbose_name_plural = 'Get Inspired Images'

    def __str__(self):
        return self.name


class Faq(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    question = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, default='draft', max_length=20)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question


class ContactUsPage(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=12, null=True, blank=True)
    division = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    call_center_info = models.TextField(null=True, blank=True)
    call_center_phone = models.CharField(max_length=100, null=True, blank=True)
    electronic_support = models.TextField(null=True, blank=True)
    electronic_email = models.EmailField(null=True, blank=True)
    electronic_ticket_link = models.URLField(max_length=300, null=True, blank=True)
    electronic_ticket = models.CharField(max_length=250, null=True, blank=True)
    map_snippet = models.TextField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us Page'

    def __str__(self):
        return self.street
