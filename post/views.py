from django.shortcuts import render, redirect

from .models import Post
from .forms import PostCreationForm


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def create(request):
    form = PostCreationForm()
    if request.method == 'POST':
        form = PostCreationForm(data=request.POST, files=request.FILES)
        ext = str(request.FILES.get('img_or_vid')).split('.')[-1]
        if form.is_valid():
            new_post = form.save(commit=False)
            # check the file extension is video extension
            if ext.lower() == 'mp4':
                new_post.type = 'video'
            new_post.save()
            return redirect(home)
    return render(request, 'form.html', {'form':form})
