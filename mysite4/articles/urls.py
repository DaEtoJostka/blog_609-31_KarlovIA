from django.urls import path
from . import views

# Define app_name for namespacing
app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<slug:slug>/', views.article_item, name='detail'),
] 