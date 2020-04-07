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
        'wishes': Wish.objects.all(),
        'posted_user': Wish.objects.filter(posted_by_id=request.session['user_id']),

    }
    return render (request, 'belt/dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def delete(request, wish_id):
    j = Wish.objects.get(id=wish_id)
    j.delete()
    return redirect ('/dashboard')

def new(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'belt/new.html', context)

def new_wish(request):
    f = request.POST
    valid = True
    if len(f['item']) < 3:
        messages.error(request, "Wish must be at least 3 characters.")
        valid = False
    if len(f['description']) < 1:
        messages.error(request, "Description must be provided.")
        valid = False
    if len(f['description']) < 3:
        messages.error(request, "Description must be at least 3 characters.")
        valid = False

    if not valid:
        return redirect ('/dashboard')

    else:
        w = Wish()
        w.granted_id = "0"
        # w.liked_by = "0"
        w.item = f['item']
        w.description = f['description']
        w.posted_by = User.objects.get(id=request.session['user_id'])
        w.save()

        messages.success(request, "Wish added!")

    return redirect('/dashboard')

def grant(request, wish_id):
    w = Wish.objects.get(id=wish_id)
    w.granted_id = request.session['user_id']
    w.save()
    return redirect ('/dashboard')

def edit(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    user = User.objects.get(posted_user=wish_id)
    context = {
        'wish': wish,
        'user': user,
    }

    return render(request, 'belt/edit.html', context)

def edit_wish(request, wish_id):
    f = request.POST
    valid = True
    if len(f['item']) < 3:
        messages.error(request, "Wish must be at least 3 characters.")
        valid = False
    if len(f['description']) < 3:
        messages.error(request, "Description must be at least 3 characters.")
        valid = False

    if not valid:
        return redirect ('/edit/' + str(wish_id))

    else:
        wish = Wish.objects.get(id=wish_id)
        wish.item=f['item']
        wish.description=f['description']
        wish.save()
        messages.success(request, "Wish updated successfully!")

    return redirect('/dashboard')

def like(request, wish_id):
    this_wish = Wish.objects.get(id=wish_id)
    this_user = User.objects.get(id=request.session['user_id'])
    this_wish.liked_by.add(this_user)
    this_wish.save()
    return redirect ('/dashboard')

# def stats(request, user_id):
#     context = {
#         'user': User.objects.get(id=user_id),
#         'wishes': Wish.objects.all(),
#         'posted_user': Wish.objects.filter(posted_by_id=request.session['user_id']),
#         'granted_wish': Wish.objects.filter(granted_id=request.session['user_id'])
        
#     }

#     return render(request, 'belt/stats.html', context)


def stats(request):
    user = User.objects.get(id= request.session['user_id'])
    context = {
        'user': user,
        'wish': Wish.objects.all()
    }

    return render(request, 'belt/stats.html', context)