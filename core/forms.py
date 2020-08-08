from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Url

class UrlInputForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ("target_url",)
        widgets = {
            'target_url': forms.TextInput(
				attrs = {
					'class': 'form-control',
                    'id': 'target-url',
                    'placeholder': 'URL',
				}
			),
        }
        labels = {
            'target_url': _('Enter a long URL to make a short URL:'),
        }