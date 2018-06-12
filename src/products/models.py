from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from multiselectfield import MultiSelectField


class Brand(models.Model):
    CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='product/brand/%Y/%m/%d/')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=CHOICES, default='draft')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CategoryGroup(models.Model):
    GROUPS = (
        ('men', 'Men'),
        ('ladies', 'Ladies'),
        ('kids', 'Kids')
    )
    name = models.CharField(choices=GROUPS, max_length=20, null=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category Group'
        verbose_name_plural = 'Category Groups'

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    name = models.CharField(max_length=250)
    cat_group = models.ForeignKey(CategoryGroup, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='product/category/%Y/%m/%d/', null=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=CHOICES, default='draft')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class Colours(models.Model):
    name = models.CharField(max_length=20, default='blue')
    color_code = models.CharField(max_length=20, help_text='visit https://www.w3schools.com/colors/colors_picker.asp',
                                  null=True, blank=True)

    class Meta:
        verbose_name = 'colour'
        verbose_name_plural = 'colours'

    def __str__(self):
        return self.name


class Product(models.Model):
    TAGS = (
        ('sale', 'Sale'),
        ('new', 'New'),
        ('gift', 'Gift'),
        ('stock', 'Stock'),
    )
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    sub_title = models.TextField(null=True, blank=True)
    price = models.FloatField(blank=True, null=True)
    new_price = models.FloatField(blank=True, null=True)
    first_image = models.ImageField(upload_to='product/item/%Y/%m/%d/', null=True, blank=True)
    second_image = models.ImageField(upload_to='product/item/%Y/%m/%d/', null=True, blank=True)
    third_image = models.ImageField(upload_to='product/item/%Y/%m/%d/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    tags = MultiSelectField(choices=TAGS, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    material = models.CharField(max_length=250, null=True, blank=True)
    size = models.CharField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)
    colours = models.ForeignKey(Colours, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    sold = models.IntegerField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductShareLinks(models.Model):
    SITES = (
        ('facebook', 'Facebook'),
        ('google-plus', 'Google+'),
        ('twitter', 'Twitter'),
        ('email', 'Email'),
    )
    sitename = models.CharField(max_length=25, null=True, blank=True, choices=SITES)
    sharelink = models.URLField(null=True, blank=True, max_length=300)
    create = models.DateTimeField(null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Share Link'
        verbose_name_plural = 'Share Links'

    def __str__(self):
        return self.sitename
