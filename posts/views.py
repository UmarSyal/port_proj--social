from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from posts.forms import PostForm

# Create your views here.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('posts:post_detail', kwargs={"username": self.request.user.username, "pk":self.object.id})

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete_confirm.html"
    
    def get_success_url(self):
        return reverse_lazy('posts:post_list')

class PostsByUserView(ListView):
    model = Post
    template_name = "posts/user_posts.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super(PostsByUserView, self).get_queryset()
        return queryset.filter(author__username=self.kwargs['username'])

class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    ordering = ['-created_on']