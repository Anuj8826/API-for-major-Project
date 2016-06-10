from receipt.models import Receipt
import json
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import ReceiptSerializer
from rest_framework.decorators import detail_route
from rest_framework import renderers
from rest_framework.request import Request

from receipt.models import Receipt
from receipt.serializers import ReceiptSerializer

from rest_framework import generics
from rest_framework import permissions
#from receipt.permissions import IsOwnerOrReadOnly


class ReceiptList(generics.ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    

class ReceiptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

