from rest_framework import serializers
from .models import Receipt
from authen.serializers import UserSerializer
from authen.models import User


class ReceiptSerializer(serializers.ModelSerializer):

  #  user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Receipt
 
        fields = ('id','merchant_name', 'price', 'date', 'receipt','status_receipt',)
        readonly_fields = ('id',)

    