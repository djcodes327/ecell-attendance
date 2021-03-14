from django.urls import path, include
from rest_framework import routers

from .views import StudentViewSet,MachineViewSet

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'machine', MachineViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_attendance'))

]

