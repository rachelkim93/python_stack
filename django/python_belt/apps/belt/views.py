from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.messages import get_messages
from django.contrib import messages
import re
from .models import User, Quote

# Create your views here.

def index(request):
    return render(request, "belt/index.html")
    
def users(request, user_id):
    author = User.objects.get(id=user_id)
    context = {
        'quotes': Quote.objects.filter(author = author),
        'author': author 
    }
    return render(request, "belt/users.html", context)

def quotes(request):
    registered_users = User.objects.all()
    current_user = User.objects.get(id = request.session['id']) 
    allquotes = Quote.objects.all().order_by('-id')
    context = {
        "registered_users": registered_users,
        "current_user": current_user,
        "quotes": allquotes,
    }
    return render(request, "belt/quotes.html", context)

def account(request):
    return render(request, 'belt/myaccount.html')

# def edit
def update(request):
    f = request.POST
    valid = True
    if len(f['first_name']) < 1:
        messages.error(request, "First name must not be empty.")
        valid = False
    if len(f['last_name']) < 1:
        messages.error(request, "Last name must not be empty.")
        valid = False
    if not EMAIL_REGEX.match(f['email']):
        messages.error(request, "Email not valid.")
        valid = False

    if not valid: return redirect ('/')
    
    else:
        if User.objects.filter(email=f['email']).exists():
            messages.error(request, "Email already exists.")
            return redirect ('/account')

        user = User.objects.get(id=request.session['user_id'])
        user.first_name = f['first_name']
        user.last_name = f['last_name']
        user.email = f['email']
        user.save()

        messages.success(request, "Account successfully edited.")
        # request.session['user_id'] = user_id
        # request.session['first_name'] = first_name

    return redirect('/dashboard')




def register(request):
    if request.method == "GET":
        return redirect ('/')
    new_user = User.objects.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['password_confirmation'])
    if new_user['status'] == True:
        request.session['id'] = new_user['created_user'].id
        return redirect('/quotes')
    else:
        messages.error(request, new_user['errors'], extra_tags = "register")
        return redirect ('/')

def login(request):
    if request.method == "GET":
        return redirect ('/')
    current_user = User.objects.login_validate(request.POST['email'], request.POST['password'])
    if current_user['status'] == True:
        request.session['id'] = current_user['found_user'].id
        return redirect('/quotes')
    else:
        messages.error(request, current_user['errors'], extra_tags = "login")
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def quote_post(request):
    if request.method == "GET":
        return redirect ('/')
    if request.method == "POST":
        quote_text = request.POST['quote']
        user_id = request.session['id']
        quoted_by = request.POST['quote_author']
        print (quoted_by)
        result = Quote.objects.validate_quote(quote_text, user_id, quoted_by)
        if result['status'] == True:
            messages.info(request, result['errors'])
            return redirect ('/quotes')
        messages.error(request, result['errors'], extra_tags = "quote_post")
        return redirect('/quotes')

def dashboard(request):
    return redirect('/quotes')

def delete(request, quote_id):
    q = Quote.objects.get(id=quote_id)
    q.delete()
    return redirect('/dashboard')


def liked(request, quote_id):
    this_quote = Quote.objects.get(id=quote_id)
    this_user = User.objects.get(id=request.session['user_id'])
    this_quote.liked_by.add(this_user)
    this_quote.save()
    return redirect ('dashboard')


def dashboard(request):
    user = User.objects.