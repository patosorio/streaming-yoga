from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        """
        add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {'email': 'Email Address'}

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
