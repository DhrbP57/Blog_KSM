from django.shortcuts import render, get_object_or_404
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

def AboutView(request):
    return render(request, 'about.html')
def ContactView(request):
    return render(request, 'contact.html')
def AchievementsView(request):
    return render(request, 'achievements.html')



def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = ImagePost.objects.filter(post=post)
    return render(request, 'article_details.html', {'posts':post, 'photos':photos})

