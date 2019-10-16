from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from users.models import DjUser
from users.serializers import DjUserSerializer

class UserList(APIView):
    
    def get(self, request):
        users = DjUser.objects.all()
        serializer = DjUserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DjUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data(), status=status.HTTP_400_BAD_REQUEST)

class User(APIView):
    
    def get_object(self, pk):
        try:
            return DjUser.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = DjUserSerializer(user, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = DjUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        