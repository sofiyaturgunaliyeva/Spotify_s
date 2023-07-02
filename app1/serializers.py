from rest_framework import serializers

from .models import *

class QoshiqchiSerializer(serializers.Serializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'



class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'
# 4.Qo’shiqdagi fayl ustuni qiymati “.mp3” bilan tugamasa ValidationError beruvchi
# validation yozing


# 5. Qo’shiq davomiyligi “00:07:00” dan ortib ketsa ValidationError beruvchi
# validation yozing


class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'

    def validate_nom(self, nom):
        if ".mp3" in nom:
            return nom
        raise serializers.ValidationError("Qo'shiq nomida xatolik")


    def validate_davomiylik(self, davomiylik):
        if davomiylik.total_seconds() <= 420:  # 7 minutdan kam bo'lsa
            return davomiylik
        raise serializers.ValidationError("Qo'shiq davomiyligi 7 minutdan uzun bo'lishi mumkin emas")

