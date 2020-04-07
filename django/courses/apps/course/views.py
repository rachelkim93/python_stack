from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Course

def update(request, id):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')

# Create your views here.
def index(request):
    context = { "courses" : Course.objects.all()}
    return render(request, 'coursesapp/index.html', context)

def addcourse(request):
    Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
    return redirect('/')

def removecourse(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, 'coursesapp/remove.html', context)

def removethis(request, id):
    this = Course.objects.get(id=id)
    this.delete()
    return redirect('/')