from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = ['hello', 'Hello World', '123', 'bye']
        return Response({'data': an_apiview})
