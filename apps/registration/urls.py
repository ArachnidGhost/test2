from django.urls import path
from .views import UserDataListCreateView, UserDataDetailView

urlpatterns = [
    path('userdata/', UserDataListCreateView.as_view(), name='userdata-list-create'),
    path('userdata/<int:pk>/', UserDataDetailView.as_view(), name='userdata-detail'),
]
