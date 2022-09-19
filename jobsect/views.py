import email
from django.shortcuts import render


# Create your views here.

def join(request):
    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        
        site = request.POST['site']
        comment = request.POST['comment']
        first_name = request.POST['first_name']
        
        
        
        
    else:
        return render(request , 'join.html')
