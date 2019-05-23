from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def heading(request):
    return HttpResponse("<em>THIS IS A FUCKING TEXT</em>")

