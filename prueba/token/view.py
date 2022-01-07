# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandardUser

#Serializers
from token.serializers import (TokenModelSerializer, TokenSerializer)

class TokenViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = TokenModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = TokenSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        exp = serializer.save()
        data = TokenModelSerializer(exp).data
        return Response(data, status=status.HTTP_201_CREATED)
        