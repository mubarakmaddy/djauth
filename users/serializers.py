from rest_framework import serializers
from users.models import DjUser

class DjUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjUser
        fields = '__all__'
        