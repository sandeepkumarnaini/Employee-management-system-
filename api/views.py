from django.shortcuts import render
from dbapp.models import Employee
import json
from .serializer import empserializer,customserializer,userserializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
# Create your views here.

def calculate(d):
    d["bonus"]=d["empsal"]*0.1

@api_view(['GET','POST'])
def apiview(request):
    if request.method=='GET':
        emp=Employee.objects.all()
        emp_data=[{'empno':obj.empno,'empname':obj.empname,'empsal':obj.empsal} for obj in emp]
        #json_emp=json.dumps(emp_data)
        emp_serial=empserializer(emp_data,many=True)
        #return JsonResponse(json_emp,safe=False)
        return Response(emp_serial.data)
    if request.method=='POST':
        print(request.data)
        calculate(request.data)
        empdata=empserializer(data=request.data)
        if empdata.is_valid()==True:
            empdata.save()
            return Response(empdata.data,status=HTTP_201_CREATED)
        else:
            return Response(empdata.errors,status=HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def viewapi(request):
    if request.method=='GET':
        emp=Employee.objects.all()
        emp_data=[{'empno':obj.empno,'empname':obj.empname,'empsal':obj.empsal} for obj in emp]
        #json_emp=json.dumps(emp_data)
        emp_serial=customserializer(emp_data,many=True)
        #return JsonResponse(json_emp,safe=False)
        return Response(emp_serial.data)
    if request.method=='POST':
        print(request.data)
        calculate(request.data)
        empdata=customserializer(data=request.data)
        if empdata.is_valid()==True:
            empdata.save()
            return Response(empdata.data,status=HTTP_201_CREATED)
        else:
            return Response(empdata.errors,status=HTTP_400_BAD_REQUEST)       
        
#fetch,update,delete
@api_view(['GET','PUT','DELETE'])
def modifyapi(request,pk):
    eobj=Employee.objects.get(empno=pk)
    if request.method=='GET':
        empdata=empserializer(eobj)
        return Response(empdata.data,status=HTTP_200_OK)
    if request.method=='PUT':
        update_obj=empserializer(eobj,data=request.data)
        if update_obj.is_valid()==True:
            update_obj.save()
            return Response(update_obj.data,status=HTTP_201_CREATED)
        else:
            return Response(update_obj.data,status=HTTP_400_BAD_REQUEST)
        
    if request.method=='DELETE':
        eobj.delete()
        return Response(status=HTTP_200_OK)

@api_view(['POST'])    
def register(request):
    if request.method=='POST':
        userobj=userserializer(data=request.data)
        if userobj.is_valid()==True:
            user_obj=userobj.save()
            user_obj.set_password(userobj.validated_data['password'])
            user_obj.save()
            Token.objects.create(user=user_obj)
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(userobj.errors,status=HTTP_400_BAD_REQUEST)

class Firstapiview(APIView):
    def get(self,request):
        page=PageNumberPagination()
        page.page_size=4
        emps=Employee.objects.all()
        emp_page=page.paginate_queryset(emps,request)
        emp_obj=empserializer(emp_page,many=True)
        return page.get_paginated_response(emp_obj.data)
    def post(self,request):
        empdata=empserializer(data=request.data)
        if empdata.is_valid()==True:
            empdata.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    
class Firstgenericview(ListAPIView):
    pagination_class=PageNumberPagination
    queryset=Employee.objects.all()
    serializer_class=empserializer

class listcreateapiview(ListCreateAPIView):
    pagination_class=PageNumberPagination
    queryset=Employee.objects.all()
    serializer_class=empserializer

class fetchupdatedelete(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=empserializer

class firstviewset(ViewSet):
    def list(self,request):
        emps=Employee.objects.all()
        empdata=empserializer(emps,many=True)
        return Response(empdata.data,status=HTTP_200_OK)
    def retrieve(self,request,pk):
        emp=Employee.objects.get(empno=pk)
        empData=empserializer(emp)
        return Response(empData.data,status=HTTP_200_OK)
