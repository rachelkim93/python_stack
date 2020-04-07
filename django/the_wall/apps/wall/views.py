from django.shortcuts import render, HttpResponse
from .models import Comment, Message

def index(request):
    return render(request, 'wall/index.html')