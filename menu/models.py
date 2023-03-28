from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
import cloudinary

STATUS = ((0, "Draft"), (1, "Published"))

MENU_CATEGORIES = (
    ('starter', 'starter'),
    ('main', 'main'),
    ('desert', 'desert'),
    )


class MenuItem(models.Model):
    """
    The model for menu items
    """

    title = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField(
        'image', default='default-menu-image_eeth2z.png'
        )
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


@receiver(pre_save, sender=MenuItem)
def get_old_cloudinary_img(sender, instance, *args, **kwargs):
    """
    Gets the current image for the instance before the save
    if it is an update
    """

    try:
        old_img = sender.objects.get(id=instance.id).featured_image.public_id
    except MenuItem.DoesNotExist:
        old_img = None

    instance.old_img = old_img


@receiver(post_save, sender=MenuItem)
def dlte_old_cloudinary_img_on_update(sender, instance, *args, **kwargs):
    """
    Deletes the old image in cloudinary if it has been updated
    unless it is the default image
    """

    try:
        new_img = instance.featured_image.public_id
    except AttributeError:
        new_img = None

    if (instance.old_img and
            instance.old_img != new_img and
            instance.old_img != 'default-menu-image_eeth2z'):

        cloudinary.uploader.destroy(instance.old_img)


@receiver(post_delete, sender=MenuItem)
def dlte_cloudinary_img_on_instance_dlte(sender, instance, *args, **kwargs):
    """
    Deletes the cloudinary image when the related instance is deleted
    unless it is the default image
    """
    instance_img = instance.featured_image.public_id

    if instance_img != 'default-menu-image_eeth2z':
        cloudinary.uploader.destroy(instance_img)
