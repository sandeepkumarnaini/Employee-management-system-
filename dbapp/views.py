from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Employee,Department
from django.db.models import Min,Max,Sum,Count,Avg
# Create your views here.
def dbprocess(request):
    if request.method=='GET':
        dept=Department.objects.all()
        return render(request,'dbapp/insert.html',{'dept':dept})
    if request.method=='POST':
        eno=int(request.POST['no'])
        ename=request.POST['name']
        esal=int(request.POST['sal'])
        edept=int(request.POST['dept'])
        dept_id=Department.objects.get(deptno=edept)
        e_obj=Employee(empno=eno,empname=ename,empsal=esal,department=dept_id)
        e_obj.save()
        return render(request,'dbapp/insert.html',{'msg':'data inserted successfully'})
    
def selectdb(request):
    if request.method=='GET':
        emps=Employee.objects.select_related('department')
        return render(request,'dbapp/select.html',{'emp':emps})
    if request.method=='POST':
        if request.POST['t1']=='':
            min=Employee.objects.aggregate(Min('empsal'))['empsal__min']
        else:
            min=int(request.POST['t1'])
        if request.POST['t2']=="":
            max=Employee.objects.aggregate(Max('empsal'))['empsal__max']
        else:
            max=int(request.POST['t2'])
        sal=Employee.objects.filter(empsal__range=(min,max))

        return render(request,'dbapp/select.html',{'emp':sal})
    
'''def updatedb(request):
    if request.method=='GET':
        return render(request,'dbapp/update.html')
    if request.method=='POST':
        eno=int(request.POST['no'])
        emp=Employee.objects.get(empno=eno)
        return render(request,'dbapp/update.html',{'emps':emp})
def updatedb2(request):
    if request.method=='POST':
        eno=int(request.POST['t1'])
        ename=request.POST['t2']
        esal=int(request.POST['t3'])
        emps_obj=Employee(empno=eno,empname=ename,empsal=esal)
        emps_obj.save()
        return render(request,'dbapp/update.html',{'msg':'data updated successfully'})'''
def updatedb(request,eno):
    emp=Employee.objects.get(empno=eno)
    if request.method=='GET':
        dep=Department.objects.all()
        return render(request,'dbapp/update1.html',{'emps':emp,'dept':dep})
    if request.method=='POST':
        emp.empno=int(request.POST['t1'])
        emp.empname=request.POST['t2']
        emp.empsal=int(request.POST['t3'])
        d_id=int(request.POST['dep'])
        emp.department=Department.objects.get(deptno=d_id)
        emp.save()
        return redirect('selectempurl')
def deletedb(request,eno):
    emp=Employee.objects.get(empno=eno)
    if request.method=='GET':
        
        return render(request,'dbapp/delete.html',{'emps':emp})
    if request.method=='POST':
        emp.delete()
        return redirect('selectempurl')
