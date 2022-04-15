from django import forms

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'your title'}))#default required=True, see in the doc
    body  = forms.CharField(required=False, widget=forms.Textarea(
                                                        attrs={
                                                            'placeholder': 'your description',
                                                            'class': 'new-class-name two',
                                                            'id': 'my-id-for-textarea',
                                                            'rows': 15,
                                                            'cols': 50,
                                                        } ))
    class Meta:
        model = Product
        fields = {
            'title',
            'description',
            'price'
        }