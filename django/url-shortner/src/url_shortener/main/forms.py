from django import forms
from .models import URLMap

class URLShortenForm(forms.Form):
    original_url = forms.URLField(
        label = "Enter URL to shorten",
        widget = forms.URLInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "https://example.com/very/long/url/"
            }
        )
    )