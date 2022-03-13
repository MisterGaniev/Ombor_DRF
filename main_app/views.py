from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
# Create your views here.


class OmborViewSet(ModelViewSet):
    queryset = Ombor.objects.all()
    serializer_class = OmborSerial
    permission_classes = [IsAuthenticated,]

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerial
    permission_classes = [IsAuthenticated,]

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerial
    permission_classes = [IsAuthenticated,]