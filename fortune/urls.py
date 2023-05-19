from django.urls import path
from .views import FortuneList, FortuneDetail

urlpatterns = [
    path('', FortuneList.as_view(), name='fortune_list'),
    path('<int:pk>', FortuneDetail.as_view(), name='fortune_detail'),
]
