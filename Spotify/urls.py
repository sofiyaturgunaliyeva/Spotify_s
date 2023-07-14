from django.contrib import admin
from django.urls import path,include
from app1.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("albomlar",AlbomModelViewset)
router.register("qoshiqlar",QoshiqModelViewset)
router.register("qoshiqchilar",QoshiqchiModelViewset)
from drf_spectacular.views import SpectacularAPIView, \
    SpectacularRedocView, \
    SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiview_docs/', SpectacularAPIView.as_view(), name="schema"),
    path('docs/', SpectacularSwaggerView.as_view(url_name = "schema")),
    path('redoc/', SpectacularRedocView.as_view(url_name = "schema")),
    path('qoshiqchilar/', QoshiqchilarAPIView.as_view()),
    path('qoshiqchilar_api/', QoshiqchilarAPIView.as_view()),
    path('qoshiqlar_api/', QoshiqlarAPIView.as_view()),
    path('', include(router.urls)),
    path('albomlar_api/', AlbomlarAPIView.as_view()),
    path('bitta_qoshiqchi/<int:pk>/', QoshiqchiDetailView.as_view()),
    # path('bitta_qoshiq/<int:pk>/', QoshiqAPIView.as_view()),
]
