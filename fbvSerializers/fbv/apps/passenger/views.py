from apps.passenger.serializers import PassengerSerializer
from apps.passenger.models import Passenger
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def list_passenger(request):
    if request.method == "GET":
        data = Passenger.objects.all()
        serializer = PassengerSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        if request.method == "POST":
            serializer = PassengerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def passenger(request, pk):
    try:
        instance = Passenger.objects.get(id=pk)
    except Passenger.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PassengerSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = PassengerSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        instance.delete()
        return Response("passenger deleted", status=status.HTTP_204_NO_CONTENT)
