from django.forms import ModelForm
from .models import MenuItem


class MenuItemForm(ModelForm):
    """
    The form used to create and edit menu items
    """

    class Meta:
        model = MenuItem
        fields = (
            'title',
            'description',
            'category',
            'featured_image',
            'available',
            'price',
            'status'
        )
