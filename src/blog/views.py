from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Article
from .forms import ArticleModelForm

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView    
)
 
# Create your views here.
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    #success_url = '/' #same as get_success_url
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    # def get_success_url(self): #url you want to return when you create an value successfully
    #     return '/'

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() #<blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    #queryset = Article.objects.all()
    #queryset = Article.objects.filter(id__gt=1)#id greater than 1

    def get_object(self):
        id_ = self.kwargs.get("pk") #pk: primary key, is the default variable name
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_update.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("articles:article-list")

def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "articles/article_list.html", context)

def article_detail_view(request, pk):
    obj = get_object_or_404(Article, id=pk)
    context = {
        "object": obj
    }
    return render(request, "articles/article_detail.html", context)