from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class GroupListAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StudentListAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class AttendenceListAPIView(generics.ListCreateAPIView):
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = Attendence.objects.all()
        serializer = AttendenceSerializer(queryset, many=True)
        actives = Attendence.objects.filter(status = 'at time').values('student').distinct().count()
        lates = Attendence.objects.filter(status = 'late').values('student').distinct().count()
        not_came = Attendence.objects.filter(status = 'not came').values('student').distinct().count()
        data = {
            'students': serializer.data,
            'actives': actives,
            'lates': lates,
            'not came': not_came,
        }
        return Response(data, status=status.HTTP_200_OK)

class AttendenceRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer

class LateStudentsAPIView(generics.ListAPIView):
    queryset = Attendence.objects.filter(status = 'late')
    serializer_class = AttendenceSerializer
    # def get(self, request, *args, **kwargs):
    #     queryset = Attendence.objects.filter(status = 'late').values('time')
    #     data = {
    #         'students': serializer.data,
    #         'actives': actives,
    #         'lates': lates,
    #         'not came': not_came,
    #     }
    #     return Response(data, status=status.HTTP_200_OK)

class AttimeStudentsAPIView(generics.ListAPIView):
    queryset = Attendence.objects.filter(status = 'at time')
    serializer_class = AttendenceSerializer

class NotStudentsAPIView(generics.ListAPIView):
    queryset = Attendence.objects.filter(status = 'not came')
    serializer_class = AttendenceSerializer

class ApsentListAPIView(generics.ListCreateAPIView):
    queryset = Apsent.objects.all()
    serializer_class = ApsentSerializer

