from django.shortcuts import render
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status, filters

from rest_framework.viewsets import ModelViewSet


# Vazifa
# 1. Hamma modellar uchun serializerlar yozib olgandan so’ng hamma
# qo’shiqchilarni chiqaruvchi API yozing
#  2. Yangi qo’shiqchi qo’shuvchi API yozing.




# Yangi vazifadan

# 1.  1. Spotify loyihasida qo’shiqchilarni ismi, davlati bo’yicha qidirish,
# tug’ilgan yili bo’yicha tartiblash imkoniyatlarini qo’shing.
class QoshiqchilarAPIView(APIView):
    def get(self, request):
        soz = request.query_params.get('qidiruv')
        if soz:
            qoshiqchilar = Qoshiqchi.objects.filter(ism__contains=soz) | Qoshiqchi.objects.filter(
                davlat=soz
            ).order_by('tugilgan_yil')
        else:
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


# Yangi vazifadan . 3. Qo’shiqlarni davomiylik bo’yicha tartiblash, nom va janr bo’yicha qidirish imkoniyatlarini qo’shing.

class QoshiqlarAPIView(APIView):
    def get(self, request):
        soz = request.query_params.get('qidiruv')
        if soz:
            qoshiqlar = Qoshiq.objects.filter(nom__contains=soz) | Qoshiq.objects.filter(
                janr=soz
            ).order_by('davomiylik')
        else:
            qoshiqlar = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)

# class QoshiqAPIView(APIView):
#     def get(self, request, pk):
#         qoshiq = Qoshiq.objects.get(id=pk)
#         serializer = QoshiqSerializer(qoshiq)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         qoshiq = Qoshiq.objects.get(id=pk)
#         malumot = request.data
#         serializer = QoshiqSerializer(qoshiq, data=malumot)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Yangi vazifadan
#  2. Albomni nomi bo’yicha qidirish, sanasi bo’yicha tartiblash imkoniyatini qo’shing.

class AlbomlarAPIView(APIView):
    def get(self, request):
        soz = request.query_params.get('qidiruv')
        if soz:
            albomlar = Albom.objects.filter(nom__contains=soz).order_by('sana')

        else:
            albomlar = Albom.objects.all()
        serializer = AlbomSerializer(albomlar, many=True)
        return Response(serializer.data)






# Vazifa

# 1. Albomlar uchun ModelViewSet yozing

# 2. Bitta albomdan turib unga tegishli qo’shiq qo’shuvchi action qo’shing.

# 3. Bitta albomdan turib unga tegishli qo’shiqlarni chiqaruvchi action qo’shing


# Yangi vazifadan
#  2. Albomni nomi bo’yicha qidirish, sanasi bo’yicha tartiblash imkoniyatini qo’shing.
class AlbomModelViewset(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # qidiruv uchun
    search_fields = ['nom']  # '__all__'    Nom va janr orqali qidiradi
    ordering_fields = ['sana']  # tartiblab chiqaradi

    @action(detail=True, methods=['Get','POST'])
    def qoshiqlar(self, request, pk): # albomlar/1/qoshiqlar
        albom = self.get_object()  # == Albom.objects.get(id = pk)
        if request.method == 'POST':
            serializer = QoshiqSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(albom=albom)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        qoshiqlar = Qoshiq.objects.filter(albom=albom)
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)


# 4. Qo’shiq jadvalini ham ModelViewSetda qayta yozing


#  Yangi vazifadan . 3. Qo’shiqlarni davomiylik bo’yicha tartiblash, nom va janr bo’yicha qidirish imkoniyatlarini qo’shing.


class QoshiqModelViewset(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # qidiruv uchun
    search_fields = ['nom', 'janr']  # '__all__'    Nom va janr orqali qidiradi
    ordering_fields = ['davomiylik']  # tartiblab chiqaradi


class QoshiqchiModelViewset(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # qidiruv uchun
    search_fields = ['ism', 'davlat']  # '__all__'    Ism va davlat orqali qidiradi
    ordering_fields = ['tugilgan_yil']  # tartiblab chiqaradi
