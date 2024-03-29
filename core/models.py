from django.db import models
from django.conf import settings

# Create your models here.


CATEGORY_CHOICES = [
    ('S', 'Shirt'),
    ('SW', 'Sport Wear'),
    ('OW', 'Out Wear')
]

LABEL_CHOICES = [
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
]


class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(
        choices=CATEGORY_CHOICES, default='NA', max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, default='P', max_length=1)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
