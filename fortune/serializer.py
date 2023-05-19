from rest_framework import serializers
from .models import Fortune


class FortuneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'owner',
            'fortune',
        )
        model = Fortune
