from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)
from .models import Post, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    context_object_name = "post_list"

    def get_queryset(self):
        status = Status.objects.get(name="published")
        return Post.objects.filter(status=status).order_by("created_on").reverse()


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title","subtitle","body","status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = "posts/details.html"
    model = Post
    context_object_name = "single_post"

    def test_func(self):
        post = self.get_object()
        if post.status.name == "archived":
            if self.request.user.is_authenticated:
                return True
        elif post.status.name == "draft":
            if self.request.user.is_authenticated:
                return self.request.user == post.author
            return False
        else:
            return True
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_post = self.object
        status = Status.objects.get(name="published")
        context['prev_post'] = Post.objects.filter(id__lt=selected_post.id)\
                                           .filter(status=status)\
                                           .order_by('-created_on')\
                                           .first()
        context['next_post'] = Post.objects.filter(id__gt=selected_post.id)\
                                           .filter(status=status)\
                                           .order_by('created_on')\
                                           .first()
        return context
        

class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/details.html"
    success_url = reverse_lazy("post_list")

class PostUpdateView(UpdateView):
    model = Post
    template_name = "posts/edit.html"
    fields = ["title","subtitle","body","status"]