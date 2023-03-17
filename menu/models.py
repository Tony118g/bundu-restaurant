from django.db import models
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

MENU_CATEGORIES = (
    ('starter', 'starter'),
    ('main', 'main'),
    ('desert', 'desert'),
    )


class MenuItem(models.Model):

    title = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(default='Menu item description')
    available = models.BooleanField(default=True)
    price = models.DecimalField(
        null=True, max_digits=4, decimal_places=2, default='00.00'
        )
    category = models.CharField(
        choices=MENU_CATEGORIES, default='main', max_length=7
        )
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
