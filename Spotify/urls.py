from django.contrib import admin
from django.urls import path,include
from app1.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("albomlar",AlbomModelViewset)
router.register("qoshiqlar",QoshiqModelViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qoshiqchilar/', QoshiqchilarAPIView.as_view()),
    path('qoshiqchilar/', QoshiqchilarAPIView.as_view()),
    # path('qoshiqlar/', QoshiqlarAPIView.as_view()),
    path('', include(router.urls)),
    # path('albomlar/', AlbomlarAPIView.as_view()),
    path('bitta_qoshiqchi/<int:pk>/', QoshiqchiDetailView.as_view()),
    # path('bitta_qoshiq/<int:pk>/', QoshiqAPIView.as_view()),
]
