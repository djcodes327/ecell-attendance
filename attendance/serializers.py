from rest_framework import serializers

from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'fname',
            'lname',
            'email',
            'phone',
            'semester',
            'gr_no',
            'enrollment_no',
            'branch',
            'status', 
            'last_login',
        ]


class MachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machines
        fields = '__all__'
