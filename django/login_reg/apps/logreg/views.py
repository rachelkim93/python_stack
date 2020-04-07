from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, 'logreg/index.html')

def register(request):
    f = request.POST
    valid = True
    if len(f['first_name']) < 2:
        messages.error(request, "First name must be at least 2 characters.")
        valid = False
    if len(f['last_name']) < 2:
        messages.error(request, "Last name must be at least 2 characters.")
        valid = False
    if len(f['email']) < 5:
        messages.error(request, "Email must be at least 5 characters.")
        valid = False
    if len(f['password']) < 8:
        messages.error(request, "Password must be at least 8 characters.")
        valid = False

    if not f['password'] == f['password_confirmation']:
        messages.error(request, "Password does not match.")
        valid = False
    
    if not valid:
        return redirect('/')

    else:
        if User.objects.filter(email=f['email']).exists():
            messages.error(request, "You are already registered.")
            return redirect ('/')

        hashed_pw = bcrypt.hashpw(f['password'].encode(), bcrypt.gensalt())
        
        User.objects.create(first_name=f['first_name'], last_name=f['last_name'], email=f['email'], password=hashed_pw)

        messages.success(request, "You registered successfully!")


    return redirect('/')

def login(request):
    f = request.POST 
    try:
        user = User.objects.get(email=f['email'])
        password_valid = bcrypt.checkpw(f['paddword'].encode(), user.password.encode())
        if password_valid:
            request.session['logged_in'] = True
            request.session['user_id'] = user.id
            messages.success(request, "You logged in.")
        else:
            message.error(request, "Password and email did not match.")
    except: 
        messages.error(request, "No user with that email.")
    return redirect ('/')


    def test(request):
        if not 'logged_in' in request.session:
            messages.erorr(request, "You need to login first.")
            return redirect ('/')
        return HttpResponse("You are logged in.")