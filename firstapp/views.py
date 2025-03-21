from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstview(request):
    if request.method=='GET':
        resp_obj=render(request,'first.html')
        return resp_obj
    if request.method=='POST':
        print(request.POST)
        v1=int(request.POST['t1'])
        v2=int(request.POST['t2'])
        if 'add' in request.POST['operation']:
            res=v1+v2
            action='addition'
        elif 'sub' in request.POST['operation']:
            res=v1-v2
            action='subtraction'
        elif 'multi' in request.POST['operation']:
            res=v1*v2
            action='multiplication'
        else:
            res=v1/v2
            action='division'
        
        return render(request,'first.html',{'result':res,'act':action})

        return HttpResponse('addition of two numbers is'+str(res))
def secondview(request):
    return HttpResponse('we are learning django')
