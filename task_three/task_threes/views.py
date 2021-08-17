from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def posts(request):
    posts = Post.objects.all()
    context = {'post': posts}
    return render(request, 'task_threes/posts.html', context)


@login_required()
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('task_threes:posts')
            image = form.instance
            context = {'form': form, 'image': image}

            return render(request, 'task_threes/new_post.html', context)
    else:
        form = PostForm()
        return render(request, 'task_threes/new_post.html', {'form': form})
