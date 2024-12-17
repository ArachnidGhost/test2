import asyncio
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserData
from .serializers import UserDataSerializer
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.utils import timezone
import datetime

# Представление для создания и получения всех данных
class UserDataListCreateView(generics.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    def create(self, request, *args, **kwargs):
        requested_time = request.data.get("time")
        if requested_time:
            requested_time = timezone.make_aware(datetime.datetime.fromisoformat(requested_time))
            requested_time = UserData.round_time(requested_time)

        if UserData.objects.filter(time=requested_time).exists():
            return Response({'error': 'Время занято'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Ваш код, который будет выполняться после создания пользователя
        self.post_creation_logic(serializer.instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def post_creation_logic(self, user):
        # Здесь ваш код, например - отправка email или другая логика
        send_mail(
            'Test Subject',
            'Test message body',
            'admin@yandex.com',
            ['kolom@email.com'],
        )

        print(f"Пользователь {user.username} был создан.")

# Представление для получения, обновления и удаления конкретного пользователя
class UserDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
