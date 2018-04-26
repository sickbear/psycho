from django.shortcuts import render, get_object_or_404

from .models import Post

def post_list(request):
    post = Post.objects.all()
    return render(request, 'post_list.html', {'posts': post})

def post_single(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_single.html', {'post': post})