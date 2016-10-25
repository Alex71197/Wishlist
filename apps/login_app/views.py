from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    result = User.objects.validate(request.POST)
    if result[0] == False:
        for message in result[1]:
            messages.add_message(request, messages.INFO, message)
        return redirect('/')

    return login_success(request, result[1])

def login(request):
    result = User.objects.login(request.POST)
    print result
    if result[0] == True:
        return login_success(request, result[1])
    else:
        messages.add_message(request, messages.INFO, result[1])
        return redirect('/')

def login_success(request, user):
    request.session['user'] = {
        'id': user.id,
        'name': user.name,
        'username': user.username
    }
    return redirect('wishlist:index')

def logout(request):
    request.session.pop('user')
    return redirect('/')
