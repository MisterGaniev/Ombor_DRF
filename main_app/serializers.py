from main_app.models import *
from rest_framework.serializers import ModelSerializer

class OmborSerial((ModelSerializer)):
    class Meta:
        model = Ombor
        fields = '__all__'

class ProductSerial((ModelSerializer)):
    class Meta:
        model = Product
        fields = '__all__'

class ClientSerial(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
