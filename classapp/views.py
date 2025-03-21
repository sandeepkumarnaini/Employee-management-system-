from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView
from dbapp.models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Firstclassview(View):
    def get(self,request):
        return render(request,'classapp/addition.html')
    def post(self,request):
        v1=int(request.POST['a'])
        v2=int(request.POST['b'])
        res=v1+v2
        return render(request,'classapp/addition.html',{'result':res})

class Secondclassview(Firstclassview):
    def post(self,request):
        m1=int(request.POST['a'])
        m2=int(request.POST['b'])
        res=m1*m2
        return render(request,'classapp/addition.html',{'result':res})

class Insertview(CreateView):
    model=Employee
    fields='__all__'
    template_name='classapp/insert.html'

    def get_success_url(self):
        return reverse('selecturl',args=str(1))
    
class selectview(ListView):
    model=Employee
    template_name='classapp/select.html'

class empupdateview(LoginRequiredMixin,UpdateView):
    login_url='loginurl'
    model=Employee
    fields='__all__'
    template_name='classapp/update.html'
    def get_success_url(self):
        return reverse('selecturl',args=str(1))