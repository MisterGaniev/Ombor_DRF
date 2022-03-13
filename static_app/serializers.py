from static_app.models import *
from rest_framework.serializers import ModelSerializer


class StaticSerial(ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'