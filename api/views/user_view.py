from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from jiibs_backend.models import Users
from api.serializers import UserSerializer
import io
import json

@csrf_exempt
def register(request):
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=UserSerializer(data=python_data)
        
        if serializer.is_valid():
            serializer.save()
            json_data=JSONRenderer().render(serializer.data)
        else:
            json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")