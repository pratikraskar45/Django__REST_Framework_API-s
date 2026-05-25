from society.models import Society
from rest_framework import serializers

class SocietySerializer(serializers.ModelSerializer):
    class Meta:
        model=Society
        fields="__all__"
        