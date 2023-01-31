from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:  # When dealing with ModelForm we need to do this
        model = Listing
        fields = [
            "title",
            "price",
            "num_bedrooms",
            "num_bathrooms",
            "square_footage",
            "address",
            "image",
        ]
