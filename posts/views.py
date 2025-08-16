from django.shortcuts import render
from django.views.generic import (
    ListView
)
from .models import Post, Status

# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    context_object_name = "post_list"

    def get_queryset(self):
        status = Status.objects.get(name="published")
        return Post.objects.filter(status=status).order_by("created_on").reverse()