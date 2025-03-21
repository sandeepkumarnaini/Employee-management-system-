from django.shortcuts import render,redirect
from .form import Addition,Insertform,userform
from . decorator import checksuperuser
from dbapp.models import Employee
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.
def addition(request):
    emptyform=Addition()
    if request.method=='GET':
        
        return render(request,'formapp/addition.html',{'form':emptyform})
    if request.method=='POST':
        dataform=Addition(request.POST)
        if dataform.is_valid()==True:
            
            v1=dataform.cleaned_data['v1']
            v2=dataform.cleaned_data['v2']
            res=v1+v2
            return render(request,'formapp/addition.html',{'result':res,'form':emptyform})
        else:
            return render(request,'formapp/addition.html',{'form':dataform})
        
def insertform(request):
    emptyform=Insertform()
    if request.method=='GET':
        return render(request,'formapp/insert.html',{'form':emptyform})
    if request.method=='POST':
        dataform=Insertform(request.POST,request.FILES)
        if dataform.is_valid()==True:
            '''eno=dataform.cleaned_data['eno']
            ename=dataform.cleaned_data['ename']
            esal=dataform.cleaned_data['esal']
            edept=dataform.cleaned_data['department']
            Employee.objects.create(empno=eno,empname=ename,empsal=esal,department=edept)'''
            dataform.save()
            messages.success(request,'yahoo')
            messages.success(request,'data inserted successfully')
            return render(request,'formapp/insert.html',{'form':emptyform})
        else:
            messages.error(request,'unfortunately')
            messages.error(request,'failed to insert data')
            return render(request,'formapp/insert.html',{'form':dataform})
@login_required(login_url='loginurl')     
def selectform(request,pno):
    if request.method=='GET':
        emps=Employee.objects.select_related('department')
        p_obj=Paginator(emps,4)
        page=p_obj.get_page(pno)
        return render(request,'formapp/select.html',{'emp':page})
    
@checksuperuser
#@user_passes_test(lambda user:user.is_superuser,login_url='selecturl')
def detailform(request,eno):
    if request.method=='GET':
        request.session.modified=True
        if 'prev' in request.session:
            request.session['prev'].append(eno)
        else:
            request.session['prev']=[eno]
        emp=Employee.objects.get(empno=eno)
        prev=Employee.objects.filter(Q(empno__in=request.session['prev']) & ~Q(empno=eno))
        return render(request,'formapp/detail.html',{'emp':emp,'pre':prev})
    
def loginform(request):
    if request.method=='GET':
        return render(request,'formapp/login.html')
    if request.method=='POST':
        name=request.POST['uname']
        pwd=request.POST['upwd']
        valid_user=authenticate(request,username=name,password=pwd)
        if valid_user==None:
            messages.error(request,'invalid credentials')
            return redirect('loginurl')
        else:
            login(request,valid_user)
            return redirect('selecturl',pno=1)
def logoutform(request):
    logout(request)
    return redirect('loginurl')

def signupform(request):
    if request.method=='GET':
        emptyform=userform()
        return render(request,'formapp/signup.html',{'emp':emptyform})
    if request.method=='POST':
        dataforms=userform(request.POST)
        if dataforms.is_valid()==True:
            dataforms.save()
            return redirect('loginurl')
        else:
            return render(request,'formapp/signup.html',{'emp':dataforms})
        