from ast import arg
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models





# Create your views here.
def index(request):
    return render(request, 'index.html' )

def join(request):
    return render(request, 'join.html' )


def insert_data(request):
    return render(request, 'insert_data' )


def insert_data(request):
    if request.method == 'POST':
        firstname  = request.POST['firstname']
        lname  = request.POST['lname']
        email  = request.POST['email']
        phone  = request.POST['phone']
        site   = request.POST['site']
        other  = request.POST['other']
        gender = request.POST['gender']
        comment= request.POST['comment']
        
        my= join(firstname=firstname, lname=lname, email=email,phone=phone
                       ,site=site,other=other, gender=gender,comment=comment)
        my.save()
        return HttpResponse("Data Saved")
    else:
        return render(request, "final/join.html")


    


