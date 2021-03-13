from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Student, Machines
from django.contrib.auth.hashers import make_password, check_password
from .serializers import StudentSerializer,MachinesSerializer


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machines.objects.all()
    serializer_class = MachinesSerializer