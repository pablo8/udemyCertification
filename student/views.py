from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from student.serializers import StudentSerializer
from student.models import Student


class ListingStudent(APIView):

    def get(self, request):
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):

    def get_object(self, request, pk):
        try:
            return Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return None

    def get(self, request, pk):
        instance = self.get_object(request, pk)
        serializer = StudentSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = self.get_object(request, pk)
        serializer = StudentSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(request, pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
