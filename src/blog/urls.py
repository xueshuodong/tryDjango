from django.urls import path
#from .views import article_list_view, article_detail_view
from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
)
app_name = 'articles'

urlpatterns = [
    #path('', article_list_view, name='article-list'),
    #path('<int:pk>/', article_detail_view, name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete')
]
