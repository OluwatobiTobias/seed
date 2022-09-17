from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthTestSerializer
from .models import User
from rest_framework.views import APIView
# from backend.auth_test import serializers
from rest_framework.exceptions import AuthenticationFailed
# from rest_framework.permissions import IsAuthenticated


class SignUp(APIView):

    def post(self, request):
        serializer = AuthTestSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(serializer.data)
            return Response(user, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignIn(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found.')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        # permission_classes = (IsAuthenticated,)

        return Response(user)


        