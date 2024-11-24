from rest_framework import serializers
from .models import *

class GroupSerializer(serializers.ModelSerializer):
    student_set = serializers.StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Group
        fields = ['name','time', 'price', 'description', 'student_set']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = "__all__"

class ApsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apsent
        fields = "__all__"
