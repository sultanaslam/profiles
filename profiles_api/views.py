from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import models
from . import permissions
from . import serializers

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        an_apiview=['hello','Hello World', '123', 'bye']
        return Response({'data': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            name = serializer.validated_data.get('name')
            message = f'Name is {name}'
            return Response({'message': message})

    def put(self, request, pk=None):
        return Response({'message':'put'})
    
    def patch(self, request, pk=None):
        return Response({'message':'patch'})
    
    def delete(self, request, pk=None):
        return Response({'message':'delete'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializers
    
    def list(self, req):
        return Response({'message':'LIST', 'data': [1,2,3,4,5]})

    def create(self, req):
        serializer = self.serializer_class(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            name = serializer.validated_data.get('name')
            message = f'Name is {name}'
            return Response({'message': message})

    def retrieve(self, request, pk=None):
        return Response({'message':'get'})
    
    def update(self, request, pk=None):
        return Response({'message':'put'})
    
    def partial_update(self, request, pk=None):
        return Response({'message':'patch'})
    
    def destroy(self, request, pk=None):
        return Response({'message':'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')


class LoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES