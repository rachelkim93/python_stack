from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if not 'gold' in request.session: 
        request.session['gold'] = 0
    
    if not 'activities' in request.session:
        request.session['activities'] = []
        
    return render(request, 'gold/index.html')

def add_gold(request):
    form = request.POST
    
    if form['building'] == 'farm': 
        new_gold = random.randint(10,20)

    elif form['building'] == 'cave': 
        new_gold = random.randint(5,10)

    elif form['building'] == 'house': 
        new_gold = random.randint(2,5)

    elif form['building'] == 'casino': 
        new_gold = random.randint(-50,50)

    request.session['gold'] += new_gold

    new_a = {}
    if new_gold > 0:
        new_a['message'] = "Earned {} gold from the {}. ({})".format(new_gold, form['building'], datetime.now())
        new_a['result'] = 'win'
    else:
        new_a['message'] = "Entered casino and lost {} gold. ({})".format(new_gold, datetime.now())
        new_a['result'] = 'lose'


    request.session['activities'].append(new_a)

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')