from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author
from .forms import PostForm, AuthorForm
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/index.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'blog/author_form.html', {'form': form})



# ...

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('index')
    


# ...

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


