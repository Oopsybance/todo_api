from rest_framework import serializers
from .models import Task

# Сериализатор для модели Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # Указываем модель, которую будем сериализовать
        fields = '__all__'  # Указываем все поля модели в качестве полей сериализатора
