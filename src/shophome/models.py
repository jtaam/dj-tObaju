from django.db import models


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

    def __str__(self):
        return self.name
