from django.shortcuts import render, redirect
from time import gmtime, strftime
import re
import random
from django.contrib import messages

from . import models


def index(request):
    return render(request,'sr_users/index.html')

def new(request):
    return render(request, 'sr_users/new.html')

def create(request):
    #validate data
    errors = User.objects.validate(request.POST)
    if (errors):
        print ("==== errror ")
        for error in errors:
            messages.error(request, errors[error])
        print (messages)
        return redirect("/users/new")
    print ("===== no errors ===")
    newU = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])

    return redirect("/users")

def update(request):
    print ("------update")
    # validate data
    errors = User.objects.validate(request.POST)
    if (errors):
        print ("==== errror ")
        for error in errors:
            messages.error(request, errors[error])
        print (messages)
        reURL = "/users/"+ str(request.POST['id']) + "/edit"
        return redirect(reURL)
    print ("===== no errors ===")

    usr = User.objects.get(id=request.POST['id'])
    print (usr)
    usr.first_name = request.POST['first_name']
    usr.last_name = request.POST['last_name']
    usr.email = request.POST['email']
    usr.save()
  
    reURL = "/users/" + str(usr.id)
    return redirect(reURL)

def destroy(request, uid):

    usr = User.objects.get(id=uid)
    usr.delete()
    return redirect('/users')

def show(request, uid):
    context = {
        'user': User.objects.get(id=uid),
    }

    return render(request,'sr_users/view.html', context)

def edit(request, uid):
    context = {
        'user': User.objects.get(id = uid),
    }

    return render(request, 'sr_users/edit.html', context)