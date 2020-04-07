from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    return render(request, 'quote_dash/index.html')

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
        user = User.objects.get(email = f['email'])
        password_valid = bcrypt.checkpw(f['password'].encode(), user.password.encode())
        if password_valid:
            request.session['logged_in'] = True
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            messages.success(request, 'You logged in.')
            return redirect('/dashboard')
        else:
            messages.error(request, "Password/email did not match.")
    except User.DoesNotExist:
        messages.error(request, 'Could not find user with that email.')
    except:
        messages.error(request, 'Something else went wrong.')
    return redirect('/')

def dashboard(request):
    if not 'user_id' in request.session:
        return redirect('/')
    user = User.objects.get(id = request.session['user_id'])
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'quotes': Quote.objects.all(),
        'posted_quotes': Quote.objects.filter(posted_by_id=request.session['user_id']),
    }
    return render(request, 'quote_dash/dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def add(request):
    f = request.POST
    valid = True
    if len(f['author']) < 3:
        messages.error(request, 'Author must be at least 3 characters.')
        valid = False
    if len(f['quote']) < 10:
        messages.error(request, 'Quote must be at least 10 characters.')
        valid = False

    if not valid:
        return redirect('/dashboard')

    else:
        q = Quote()
        q.author=f['author']
        q.quote=f['quote']
        q.posted_by=User.objects.get(id=request.session['user_id'])
        q.save()

        messages.success(request, 'Quote successfully added!')

    return redirect('/dashboard')

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
        'quotes': Quote.objects.filter(posted_by_id=user_id)
    }
    return render(request, 'quote_dash/user_quotes.html', context)

def edit_account(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
    }
    return render(request, 'quote_dash/edit_account.html', context)


def delete(request, quote_id):
    q = Quote.objects.get(id=quote_id)
    q.delete()
    return redirect('/dashboard')


def edit(request, user_id):
    f = request.POST
    valid = True
    if len(f['first_name']) < 1:
        messages.error(request, 'First name must not be left blank.')
        valid = False
    if len(f['last_name']) < 1:
        messages.error(request, 'Last name must not be left blank.')
        valid = False
    if not EMAIL_REGEX.match(f['email']):
        messages.error(request, 'Invalid email address.')
        valid = False

    if not valid:
        return redirect('/')

    else:
        if User.objects.filter(email=f['email']).exists():
            messages.error(request, 'Email already exists.')
            return redirect('/')

        user = User.objects.get(id=request.session['user_id'])
        user.first_name=f['first_name']
        user.last_name=f['last_name']
        user.email=f['email']
        user.save()

        messages.success(request, 'Account successfully edited!')
        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name

    return redirect('/dashboard')

def like(request, quote_id):
    this_quote = Quote.objects.get(id=quote_id)
    this_user = User.objects.get(id=request.session['user_id'])
    this_quote.liked_by.add(this_user)
    this_quote.save()
    return redirect('/dashboard')