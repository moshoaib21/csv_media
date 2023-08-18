from rest_framework import serializers
from .models import csvfile

class MyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = csvfile
        fields = '__all__'