from django.shortcuts import render, redirect
from .models import Project, Like, Comment
from .forms import LikeForm, CommentForm

def index(request):
    return render(request, 'index.html')

def portfolio_view(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    likes = project.like_set.all()
    comments = project.comment_set.all()
    
    if request.method == 'POST':
        if 'like' in request.POST:
            like_form = LikeForm(request.POST)
            if like_form.is_valid():
                like = like_form.save(commit=False)
                like.project = project
                like.user = request.user
                like.save()
                return redirect('project_detail', project_id=project_id)
        else:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.project = project
                comment.user = request.user
                comment.save()
                return redirect('project_detail', project_id=project_id)
    else:
        like_form = LikeForm()
        comment_form = CommentForm()

    return render(request, 'project_detail.html', {'project': project, 'likes': likes, 'comments': comments, 'like_form': like_form, 'comment_form': comment_form})