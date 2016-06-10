from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import User, USER_TYPE, Group
from .serializers import UserSerializer, OwnerSerializer
import json
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token


@api_view(['GET', 'POST'])
@csrf_exempt
@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def user_list(request):
    """
    List all users, or create a user.
    """
    if request.method == 'GET':
        params = {
        'is_active': True
        }
        if 'group' in request.GET:
            try:
                params['groups__name'] = USER_TYPE[request.GET['group']]
            except KeyError:
                return Response({'message': "invalid group"}, status=status.HTTP_400_BAD_REQUEST)

        users = User.objects.filter(**params)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def user_detail(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

  
    elif request.method == 'DELETE':
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
@csrf_exempt
@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def add_group(request, pk):
    try:
        u = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response("User DoesNotExist", status=status.HTTP_400_BAD_REQUEST)
    else:
        data = request.data
        print request.data['group']
        if "group" in data: #and data['group'] in USER_TYPE:
            stat = u.add_to_group(data['group'])
            if stat:
                return Response("", status=status.HTTP_201_CREATED)

        return Response("Invalid Group. options are %s" % (','.join(USER_TYPE.keys())), status=400)


@api_view(['POST'])
@csrf_exempt
@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def add_owner(request):
    # creating like this in this standard method
    # need to change properly
    # takes username, email, password
    # creates owner
    response, status = {}, 201

    serializer = OwnerSerializer(data=request.POST)

    if serializer.is_valid():
        try:
            u = serializer.save()
        except KeyError as e:
            response['message'] = str(e)
            status = 401
        except Exception as e:
            response['message'] = str(e)
            status = 400
        else:
            p = request.POST['password']
            u.set_password(p)
            u.save()
            response = {'id': u.id}
    else:
        response = serializer.errors
        status = 400

    return Response(response, status=status)



@api_view(['GET'])
@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def example_view(request, format=None):
    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),  # None
    }
    return Response(content)

