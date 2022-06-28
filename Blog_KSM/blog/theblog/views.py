from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, ImagePost

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['character_universe_list'] = ImagePost.objects.all()
        return context

class ImageView(ListView):
    model = ImagePost
    template_name = 'images.html'

