#stworzony plik

from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, ImageView, blog_view, detail_view, AboutView, ContactView, AchievementsView

urlpatterns = [
    #path('', views.home, name="home"),

    #path('', HomeView.as_view(), name="home"),
    path('images', ImageView.as_view(), name="images"),
    #path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),

    path('', views.blog_view, name='home' ),
    path('<int:id>/', views.detail_view, name='article-detail'),
    path('about', views.AboutView, name='about'),
    path('contact', views.ContactView, name='contact'),
    path('achievements', views.AchievementsView, name='achievements'),
]