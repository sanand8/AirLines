from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from booknview.models import Hotels
from .serializers import HotelSerializer

class HotelListView(ListAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer

class HotelCreate(CreateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer

class HotelDelete(DestroyAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer

class HotelUpdate(UpdateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer
