from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import Postform
from django.shortcuts import redirect

def postlist(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')   
    return render(request, 'blog/postlist.html', {'posts': posts})

def post_detail(request, pk):
       post = get_object_or_404(Post, pk=pk)
       return render(request, 'blog/post_inhoud.html', {'post': post})

def post_nieuw(request):   
     form = Postform()
     return render(request, 'blog/post_edit.html', {'form': form})

def post_nieuw(request):   
     if request.method == "POST":
       form = Postform(request.POST)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect('post_inhoud', pk=post.pk)
     else:
      form = Postform()
      return render(request, 'blog/post_edit.html', {'form': form})
