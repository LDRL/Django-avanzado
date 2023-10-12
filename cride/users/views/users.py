"""Users views"""

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework.views import APIView

#Serializers
from cride.users.serializers import (UserLoginSerializer, UserModelSerializer, UserSingUpSerializer, AccountVerificationSerializer)


class UserViewSet(viewsets.GenericViewSet):
    """
    Handle sing up, login and account verification.
    """
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sing in"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user':UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def singup(self, request):
        """User sing up"""
        serializer = UserSingUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Account verification"""

        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'mensaje':'Congratulation, now go share shome rides!'}
        return Response(data, status=status.HTTP_200_OK)