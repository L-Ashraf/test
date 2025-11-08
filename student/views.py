from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializer


from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


##post data
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)