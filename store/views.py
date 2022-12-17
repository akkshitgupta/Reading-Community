from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from store.models import Members, Wishlist

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

# def home(request):
#     return HttpResponseRedirect(reverse('index'))

def wishlist(request):
    mybooks = Wishlist.objects.all().values()
    template = loader.get_template('wishlist.html')
    context = {
        'book' : mybooks,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def check(request):
    usern = request.POST['username']
    PassW = request.POST['password']
    passw = Members.objects.filter(eMail=usern).values('passWord')
    if passw == PassW:
        # template = loader.get_template('wishlist.html')
        # return HttpResponse(template.render({}, request))
        return HttpResponse('<h1>passw</h1>')
    else:
        return HttpResponse('<h4 style="text-align:centre">wrong username or password</h4>')

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({}, request))

def addmember(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['email']
    p = request.POST['password']
    user = Members(firstName = x, lastName = y, eMail = z, passWord = p)
    user.save()
    return HttpResponseRedirect(reverse('login'))

def addToList(request):
    t = request.POST['title']
    a = request.POST['author']
    g = request.POST['genre']
    book = Wishlist(title = t, author = a, genre = g)
    book.save()
    return HttpResponseRedirect(reverse('wishlist'))





def redirect(request):
    return HttpResponseRedirect(reverse('index'))