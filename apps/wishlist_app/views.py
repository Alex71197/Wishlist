from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Item
from ..login_app.models import User

# Create your views here.
def index(request):
    context = {
        'myitems': Item.objects.filter(user = User.objects.get(id = request.session['user']['id'])),
        'allitems': Item.objects.exclude(user = User.objects.get(id = request.session['user']['id'])).exclude(join = User.objects.filter(id = request.session['user']['id'])).order_by()[::-1],
        'joinitems': Item.objects.filter(join = User.objects.filter(id = request.session['user']['id']))
    }
    return render(request, 'wishlist_app/index.html', context)

def create(request):
    return render(request, 'wishlist_app/add.html')

def home(request):
    return redirect('wishlist:index')

def create_item(request):
    result = Item.objects.validate(request.POST)
    if result:
        for error in result:
            messages.error(request, error)
        return redirect('wishlist:create')
    else:
        print request.session['user']['id']
        Item.objects.create_product(request.POST, request.session['user']['id'])
        print 'works'
        return redirect('wishlist:index')

def show_item(request, id):
    context = {
        'items': Item.objects.get(id = id)

    }
    return render(request, 'wishlist_app/show_item.html', context)

def join_item(request, id):
    print 'works'
    result = Item.objects.join_product(id, request.session['user']['id'])
    print 'works'
    return redirect('wishlist:index')

def remove_item(request, id):
    result = Item.objects.remove_product(id, request.session['user']['id'])
    return redirect('wishlist:index')

def delete_item(request, id):
    Item.objects.get(id = id).delete()
    return redirect('wishlist:index')
