from django.db import models

# Модель для задачи
class Task(models.Model):
    title = models.CharField(max_length=100)  # Поле с заголовком задачи
    description = models.TextField()  # Поле с описанием задачи
    completed = models.BooleanField(default=False)  # Поле для обозначения выполнения задачи
    deadline = models.DateField(null=True, blank=True)  # Поле с датой срока выполнения задачи
    created_at = models.DateTimeField(auto_now_add=True)  # Поле с датой создания задачи

    class Meta:
        app_label = 'tasks'  # Указываем ярлык (app_label) для модели
