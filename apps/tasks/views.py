from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

from rest_framework.permissions import IsAuthenticated


# list tasks
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def all_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# create
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_task(request):
    data = request.data
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.create(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
