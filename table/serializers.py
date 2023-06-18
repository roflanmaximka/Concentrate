from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Record


class RecordSerializer(ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
