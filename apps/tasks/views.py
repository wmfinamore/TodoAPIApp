from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

from rest_framework import permissions


# list tasks
@api_view(['GET'])
def all_tasks(request):
    tasks = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# create
@api_view(['POST'])
def create_task(request):
    data = request.data
    permission_classes = [permissions.IsAuthenticated]
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.create(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
