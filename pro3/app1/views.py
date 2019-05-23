from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def help(request):
    help_me = {'insert_help_here':'<h2>this is text from views.py</h2>'}
    return render(request,'app1/help1.html',context = help_me)



