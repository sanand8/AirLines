from django.urls import path

from booknview.api.views import (
    HotelListView,
    HotelDelete,
    HotelUpdate,
    HotelCreate
)

urlpatterns = [
    path('', HotelListView.as_view()),
    path('create/', HotelCreate.as_view()),
    path('<pk>/delete/', HotelDelete.as_view()),
    path('<pk>/update/', HotelUpdate.as_view()),
]