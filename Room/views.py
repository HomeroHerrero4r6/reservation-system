from decimal import Context
from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer
from Room.serializers import RoomSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,status
from .serializers import RoomSerializer
from .models import Room
from Room import serializers
# Create your views here.
class RoomDetail(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
class AllRooms(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    def list(self,request): 
        serializer_context = {
            'request': request,
        }       
        serializer_class = RoomSerializer(self.queryset, many=True)
        return Response(serializer_class.data)

    # @action(detail=True, methods=['post'])
    # def set_room(self,request):
    #     new_room = self.get_queryset()
    # def set_room(self, request, pk=None):
    #     room = self.get_object()
    #     serializer = RoomSerializer(data = request.data)
    #     if serializer.is_valid():
    #         room.self.set_room(serializer.validated_data['__all__'])
    #         room.save()
    #         return Response({'status':'set_room'})
    #     else:
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # @action(detail=True, methods=['patch'])
    # def set_availibility(self, request, pk=None):
    #     room = self.get_object()
    #     serializer = RoomSerializer(data=request.data)
    #     if serializer.is_valid():
    #         room.set_availibility(serializer.validated_data['abailibility'])
    #         room.abailibility = not room.abailibility
    #         room.save()
    #         return Response({'status': 'abailivility set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)
