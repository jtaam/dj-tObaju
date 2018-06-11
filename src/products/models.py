from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


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
    # CHOICES = (
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    # )
    #
    # name = models.CharField(max_length=250)
    # cat_group = models.ForeignKey(CategoryGroup, on_delete=models.CASCADE, null=True, blank=True)
    # image = models.ImageField(upload_to='product/category/%Y/%m/%d/', null=True, blank=True)
    # description = models.TextField()
    # status = models.CharField(max_length=20, choices=CHOICES, default='draft')
    # create = models.DateTimeField(auto_now_add=True)
    # update = models.DateTimeField(auto_now=True)
    #
    # def __str__(self):
    #     return self.name
    pass


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
    pass
