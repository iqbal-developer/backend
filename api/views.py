from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.
def home(request):
    return HttpResponse("This is the homepage")

class TaskViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        task = queryset.get(pk=pk)
        serializer = self.serializer_class(task)
        return Response(serializer.data)

    def update(self, request, pk=None, partial=False):
        queryset = self.get_queryset()
        task = queryset.get(pk=pk)
        serializer = self.serializer_class(task, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        task = queryset.get(pk=pk)
        task.delete()
        return Response(status=204) 
    