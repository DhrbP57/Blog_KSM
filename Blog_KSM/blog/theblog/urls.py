#stworzony plik

from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, ImageView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('images', ImageView.as_view(), name="images"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),

]