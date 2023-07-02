from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import  status


# Vazifa
# 1. Hamma modellar uchun serializerlar yozib olgandan so’ng hamma
# qo’shiqchilarni chiqaruvchi API yozing
#  2. Yangi qo’shiqchi qo’shuvchi API yozing.

class QoshiqchilarAPIView(APIView):
    def get(self, request):
        qoshiqchilar = Qoshiqchi.objects.all()
        serializer = QoshiqchiSerializer(qoshiqchilar, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = QoshiqchiSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 3. Biron qo’shiqchini o’zgartiruvchi, o’chiruvchi API’lar yozing

class QoshiqchiDetailView(APIView):
    def put(self,request,pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        malumot = request.data
        serializer = QoshiqchiSerializer(qoshiqchi, data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Qoshiqchi.objects.filter(id=pk).delete()
        return Response({"xabar": "Qo'shiq ma'lumoti o'chirildi1"}, status=status.HTTP_204_NO_CONTENT)




class QoshiqlarAPIView(APIView):
    def get(self, requset):
        qoshiqlar = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)

class QoshiqAPIView(APIView):
    def get(self, request, pk):
        qoshiq = Qoshiq.objects.get(id=pk)
        serializer = QoshiqSerializer(qoshiq)
        return Response(serializer.data)

    def put(self, request, pk):
        qoshiq = Qoshiq.objects.get(id=pk)
        malumot = request.data
        serializer = QoshiqSerializer(qoshiq, data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)