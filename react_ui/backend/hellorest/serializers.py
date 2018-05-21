from rest_framework_json_api import serializers
from .models import HelloRestProcess


class HelloRestProcessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HelloRestProcess
        fields = '__all__'
