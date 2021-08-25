from django import shortcuts
from django.conf import settings
from django.db import models
from django.shortcuts import reverse



CATEGORY_CHOICES = {
    ('A', 'Áo'),
    ('Q', 'Quần'),
    ('PK', 'Phụ kiện')
}

LABEL_CHOICES = {
    ('P', 'primary'),
    ('S', 'secondry'),
    ('D', 'danger')
}

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("shop:product", kwargs={
            'slug': self.slug
        })
    

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date= models.DateTimeField(auto_now_add=True)
    oder_date = models.DateTimeField()
    odered = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username