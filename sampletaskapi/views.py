from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()

    }
    return render(request, 'sampletaskapi/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'sampletaskapi/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5




class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['titles', 'content']

    def form_valid(self, form):

        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['titles', 'content']

    def form_valid(self, form):

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True



class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True


