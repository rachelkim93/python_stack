from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

stuff = {'count' : 1, 'rando': get_random_string()}

def index(request):
	return render(request, 'random_word/index.html', stuff)

def generate(request):
	stuff['count'] += 1
	stuff['rando'] = get_random_string()
	return redirect('/')

def refresh(request):
	stuff['count'] = 1
	return redirect('/')