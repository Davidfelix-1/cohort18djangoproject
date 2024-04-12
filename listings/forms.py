from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title',
                  'price',
                  'bedroom_number',
                  'bathroom_number',
                  'square_footage',
                  'address',
                  'image'
                  ]
