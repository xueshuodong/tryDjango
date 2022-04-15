from django import forms

from .models import Product

#different types of using forms...

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'your title'}))#default required=True, see in the doc
    email       = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(
                                                        attrs={
                                                            'placeholder': 'your description',
                                                            'class': 'new-class-name two',
                                                            'id': 'my-id-for-textarea',
                                                            'rows': 3,
                                                            'cols': 20,
                                                        } ))
    price       = forms.DecimalField(initial=199.99)    
    class Meta:
        model = Product
        fields = {
            'title',
            'description',
            'price'
        }
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'CFE' in title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        else:
            return email

class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'your title'}))#default required=True, see in the doc
    description = forms.CharField(required=False, widget=forms.Textarea(
                                                        attrs={
                                                            'placeholder': 'your description',
                                                            'class': 'new-class-name two',
                                                            'id': 'my-id-for-textarea',
                                                            'rows': 3,
                                                            'cols': 20,
                                                        }))
    price       = forms.DecimalField(initial=199.99)