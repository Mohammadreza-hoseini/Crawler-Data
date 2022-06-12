from rest_framework import serializers
from .models import EsgScore, Companies


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__'


class EsgScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = EsgScore
        fields = '__all__'
