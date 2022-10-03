
from django.shortcuts import render
from rest_framework import viewsets

from first_app.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        queryset = Student.objects.all()
        user =  get_object_or_404(queryset,pk=pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)

    def create(self,request): 
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except:
            return Response(serializer.errors)

    def update(self,request,pk):
        queryset = Student.objects.all()
        user =  get_object_or_404(queryset,pk=pk)
        serializer = StudentSerializer(user,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def partial_update(self,request,pk):
        queryset = Student.objects.all()
        user =  get_object_or_404(queryset,pk=pk)
        serializer = StudentSerializer(user,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)







