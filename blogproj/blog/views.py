from django.shortcuts import render, redirect
from .models import postModel
from .forms import postModelForm, PostUpdateForm

# Create your views here.

def index(request):
     posts = postModel.objects.all()
     if request.method == 'POST':
          form = postModelForm(request.POST)
          if form.is_valid():
              instance = form.save(commit=False)
              instance.author = request.user
              instance.save()
              return redirect('blog-index')
     else:
          form = postModelForm()
     form = postModelForm()
     context = {
          'posts': posts,
          'form': form
     }
     return render(request, 'blog/index.html', context)

def post_details(request,pk):
     post = postModel.objects.get(id=pk)
     context = {
          'post' : post,
     }
     return render(request, 'blog/post_details.html', context)

def post_edit(request,pk):
     post = postModel.objects.get(id=pk)
     if request.method == 'POST':
          form = PostUpdateForm(request.POST, instance=post)
          if form.is_valid():
               form.save()
               return redirect('blog_post_details', pk=post.id)
     else:
          form = PostUpdateForm(instance=post)
     context = {
          'post':post,
          'form':form,
     }
     return render(request, 'blog/post_edit.html', context)

def post_delete(request, pk):
     post = postModel.objects.get(id=pk)
     if request.method == 'POST':
          post.delete()
          return redirect('blog-index')
     context = {
          'post':post,
     }
     return render(request, 'blog/post_delete.html',context)
     