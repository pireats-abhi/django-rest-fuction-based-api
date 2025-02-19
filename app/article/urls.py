from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('article/', views.article_list, name='article_list'),
    path('article/<int:id>/', views.article_detail, name='article_detail')
]