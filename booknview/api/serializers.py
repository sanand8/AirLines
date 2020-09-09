from rest_framework import serializers

from booknview.models import Hotels

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'