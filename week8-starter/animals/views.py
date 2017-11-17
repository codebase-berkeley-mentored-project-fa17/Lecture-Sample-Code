from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Comment

from django.http import JsonResponse

# Create your views here.
def get_info(request):
    if request.method == 'GET':
        return render(request, 'animals/get_info.html', {})

    name = request.POST['name']
    age = request.POST['age']

    return render(request, 'animals/display.html', {"name": name, "age": age})

@login_required
def kill_animals(request):
    return render(request, 'animals/kill.html', {})


@login_required
def comment(request):
    if request.method == 'POST':
        author = request.POST['author']
        text = request.POST['text']
        comment = Comment(author=author, text=text)
        comment.save()
        success = {
            "success": True
        }
        return JsonResponse(success)
    else:
        context = {"comments": Comment.objects.all()}
        return render(request, 'animals/comments.html', context)
