from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'your title'}))#default required=True, see in the doc
    content  = forms.CharField(required=False, widget=forms.Textarea(
                                                        attrs={
                                                            'placeholder': 'your content',
                                                            'class': 'new-class-name two',
                                                            'id': 'my-id-for-textarea',
                                                            'rows': 15,
                                                            'cols': 50,
                                                        } ))
    class Meta:
        model = Article
        fields = {
            'title',
            'content',
            'active'
        }