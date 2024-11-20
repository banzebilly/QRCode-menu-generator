from django import forms


class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=50, 
        label='Restaurant Name',
        #add some extra style to the input widget
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Restaurant name',
        })
    )

    url = forms.URLField(
        max_length=200, 
        label='Menu URL',

          #add some extra style to the input widget
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the URL of the online menu ',
        })
        )