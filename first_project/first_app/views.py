from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create Views Here

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpages_list}
    #my_dict = {'insert_me':"now I am coming from first_app index.html"}
    return render(request,'first_app/index.html',context=date_dict)
    