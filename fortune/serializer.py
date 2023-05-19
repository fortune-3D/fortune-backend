from rest_framework import serializers
from .models import Fortune


class FortuneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'owner',
            'fortune',
            # 'description',
            # 'hourly_sales',
            # 'minimum_customers_per_hour',
            # 'maximum_customers_per_hour',
            # 'average_cookies_per_sale'
        )
        model = Fortune
