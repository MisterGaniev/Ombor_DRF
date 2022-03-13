from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.


class StaticViewSet(ModelViewSet):
    queryset = Stats.objects.all()
    serializer_class = StaticSerial
    permission_classes = [IsAuthenticated,]