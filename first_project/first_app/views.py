from django.shortcuts import render
from django.http import HttpResponse
# Create Views Here
def index(request):
    my_dict = {'insert_me':"now I am coming from first_app index.html"}
    return render(request,'first_app/index.html',context=my_dict)
    