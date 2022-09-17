from rest_framework import serializers
from .models import User

class AuthTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "('id', 'email', 'password')"
        extra_kwargs = {'password':{'write_only': True}}

