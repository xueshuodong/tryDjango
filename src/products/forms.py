from django import forms

from .models import Product

#different types of using forms...

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            'title',
            'description',
            'price'
        }

class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={
                                                        'placeholder': 'your title'
                                                        }))#default required=True, see in the doc
    description = forms.CharField(required=False, widget=forms.Textarea(
                                                        attrs={
                                                            'placeholder': 'your description',
                                                            'class': 'new-class-name two',
                                                            'id': 'my-id-for-textarea',
                                                            'rows': 3,
                                                            'cols': 20,
                                                        }
                                                    ))
    price       = forms.DecimalField(initial=199.99)