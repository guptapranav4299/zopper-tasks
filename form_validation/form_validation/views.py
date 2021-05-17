from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer
from .models import UserModel
from django.shortcuts import redirect


@csrf_exempt
def create_user_serializer_view(request):
    if request.method == 'GET':
        user = UserModel.objects.all()
        serializer = UserSerializer(user,many = True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def get_user_details(request,pk):
    try:
        user = UserModel.objects.get(pk=pk)
    except UserModel.DoesNotExist:
        return HttpResponse(404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    


