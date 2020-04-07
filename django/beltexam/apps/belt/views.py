from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
from datetime import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    return render(request, 'belt/index.html')

def register(request):
    f = request.POST
    valid = True
    if len(f['first_name']) < 2:
        messages.error(request, 'First name must be at least 2 characters.')
        valid = False
    if len(f['last_name']) < 2:
        messages.error(request, 'Last name must be at least 2 characters.')
        valid = False
    if len(f['email']) < 8:
        messages.error(request, 'Email must be at least 8 characters.')
        valid = False
    if not EMAIL_REGEX.match(f['email']):
        messages.error(request, 'Invalid email address.')
        valid = False
    if len(f['password']) < 8:
        messages.error(request, 'Password must be at least 8 characters.')
        valid = False

    if not f['password'] == f['password_confirmation']:
        messages.error(request, 'Password and password confirm do not match.')
        valid = False

    if not valid:
        return redirect('/')

    else:
        if User.objects.filter(email=f['email']).exists():
            messages.error(request, 'You have already registered. Please login.')
            return redirect('/')

        hashed_pw = bcrypt.hashpw(f['password'].encode(), bcrypt.gensalt())

        user = User()
        user.first_name=f['first_name']
        user.last_name=f['last_name']
        user.email=f['email']
        user.password = hashed_pw
        user.save()

        messages.success(request, 'Successfully registered!')
        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name

    return redirect('/dashboard')

def login(request):
    f = request.POST
    try:
        user = User.objects.get(email=f['email'])
        password_valid = bcrypt.checkpw(f['password'].encode(), user.password.encode())
        if password_valid:
            request.session['logged_in'] = True
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            messages.success(request, "You have logged in.")
            
            return redirect ('/dashboard')
        else: messages.error(request, "Password and email do not match.")
    except:
        messages.error(request, "Something else went wrong.")
    return redirect ('/')

def dashboard(request):
    if not 'user_id' in request.session:
        return redirect ('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'jobs': Job.objects.all(),
        'posted_jobs': Job.objects.filter(posted_by_id=request.session['user_id']),

    }
    return render (request, 'belt/dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def delete(request, job_id):
    j = Job.objects.get(id=job_id)
    j.delete()
    return redirect ('/dashboard')

def view(request, user_id):
    context = {
        'jobs': Job.objects.get(id=user_id),
        'user': User.objects.get(id=request.session['user_id']),
        'category': Category.objects.filter(),
    }
    return render (request, 'belt/view.html', context)

def edit(request, job_id):
    job = Job.objects.get(id=job_id)
    user = User.objects.get(posted_jobs=job_id)
    category = Category.objects.all()
    context = {
        'job': job,
        'user': user,
        'category': category,
    }
    return render(request, 'belt/edit.html', context)

def edit_job(request, job_id):
    f = request.POST
    valid = True
    if len(f['title']) < 1:
        messages.error(request, "Job title must not be left blank.")
        valid = False
    if len(f['description']) < 1:
        messages.error(request, "Description must not be left blank.")
        valid = False
    if len(f['location']) < 1:
        messages.error(request, "Location must be not be left blank.")
        valid = False

    if not valid:
        return redirect('/edit/' + str(job_id))

    else:
        job = Job.objects.get(id=job_id)
        job.title=f['title']
        job.description=f['description']
        job.location=f['location']
        job.save()
        messages.success(request, "Job successfully updated!")

    return redirect('/dashboard')

def new(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
        'category': Category.objects.all(),
    }
    return render(request, 'belt/new.html', context)

def new_job(request):
    f = request.POST
    valid = True
    if len(f['createCat']) > 3:
        cat = Category.objects.create(name=request.POST['createCat'])
        cat.save()
        # return redirect ('/new/' + str(user_id))
    if len(f['title']) < 3:
        messages.error(request, "Job title must be at least 3 characters.")
        valid = False
    if len(f['title']) < 1:
        messages.error(request, "Job title must be filled out.")
        valid = False
    if len(f['description']) < 3:
        messages.error(request, "Description must be at least 3 characters.")
        valid = False
    if len(f['description']) < 1:
        messages.error(request, "Description must be filled out.")
        valid = False
    if len(f['location']) < 3:
        messages.error(request, "Location must be at least 3 characters.")
        valid = False
    if len(f['location']) < 1:
        messages.error(request, "Location must be filled out.")
        valid = False

    if not valid:
        return redirect('/dashboard')

    else:
        j = Job()
        j.has_job_id="0"
        j.title = f['title']
        j.description = f['description']
        j.location = f['location']
        j.posted_by = User.objects.get(id=request.session['user_id'])
        j.job_category = cat
        j.save()

        messages.success(request, "Job added!")

    return redirect('/dashboard')

def addJob(request):
    j = Job.objects.first()
    j.has_job_id = request.session['user_id']
    j.save()
    return redirect('/dashboard')

def giveUp(request):
    j = Job.objects.first()
    j.has_job_id= "0"
    j.save()
    return redirect('/dashboard')

def finishJob(request):
    j = Job.objects.first()
    j.delete()
    return redirect('/dashboard')