from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

# VIEWS #
from .serializers import TodoSerializer 
from rest_framework import viewsets      
from .models import Todo                 

class TodoView(viewsets.ModelViewSet):  
    serializer_class = TodoSerializer   
    queryset = Todo.objects.all()     
    http_method_names = ['get', 'delete', 'post']
    
    def destroy(self, request, *args, **kwargs):
        user_object = self.get_object()
        user_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)