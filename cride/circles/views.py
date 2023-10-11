"""Circles views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cride.circles.serializers import (CircleSerializer, CreateCircleSerializer)


# Models
from cride.circles.models import Circle

# self, request, *args, **kwargs


@api_view(['GET'])
def list_circles(request):
    """List circles"""
    circles = Circle.objects.filter(is_public=True)
    # data = []
    # for circle in circles:
    #     serializer = CircleSerializer(circle)
    #     data.append(serializer.data)
    serializer = CircleSerializer(circles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_circle(request):
    """Create circle."""
    # name = request.data['name']
    # slug_name = request.data['slug_name']
    # about = request.data.get('about', '')
    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    circle = serializer.save()
    return Response(CircleSerializer(circle).data)
