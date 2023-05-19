from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CookieStand
from .serializer import CookieStandSerializer
from .permissions import isOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CookieStandList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer
