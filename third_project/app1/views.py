from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    home_page = {'insert_home_content':'this content has come from views.py'}
    return render(request,'app1/home.html',context=home_page)

def index(request):
    index_page = {'insert_index_content':'this content has come from views.py on index page'}
    return render(request,'app1/index.html',context=index_page)

