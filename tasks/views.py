from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Представление для создания и получения списка задач
class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()  # Запрос к модели Task для получения всех задач
    serializer_class = TaskSerializer  # Сериализатор для преобразования данных задач в формат JSON

# Представление для получения, обновления и удаления отдельной задачи
class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()  # Запрос к модели Task для получения всех задач
    serializer_class = TaskSerializer  # Сериализатор для преобразования данных задач в формат JSON
