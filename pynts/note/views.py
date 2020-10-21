from django.views.generic import DetailView, ListView

from .models import Post

class PostListView(ListView):
    model = Post
# Create your views here.

class PostDetailView(DetailView):
    model = Post