
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qoshiqchilar/', QoshiqchilarAPIView.as_view()),
    path('qoshiqchilar/', QoshiqchilarAPIView.as_view()),
    path('qoshiqlar/', QoshiqlarAPIView.as_view()),
    path('bitta_qoshiqchi/<int:pk>/', QoshiqchiDetailView.as_view()),
    path('bitta_qoshiq/<int:pk>/', QoshiqAPIView.as_view()),
]
