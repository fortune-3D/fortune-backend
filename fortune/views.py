from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Fortune
from .serializer import FortuneSerializer
from .permissions import isOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class FortuneList(ListCreateAPIView):
    permission_classes = [] # (IsAuthenticated,)
    queryset = Fortune.objects.all()
    serializer_class = FortuneSerializer


class FortuneDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [] # (IsAuthenticated,)
    queryset = Fortune.objects.all()
    serializer_class = FortuneSerializer
