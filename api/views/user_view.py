from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from jiibs_backend.models import Users
from rest_framework import permissions,status
from api.serializers import UserSerializer
from rest_framework.response import Response
import io
import json
from django.db import connection

def dictfetchall(cursor):
    #"Returns all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
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

@csrf_exempt
def login(request):
    if request.method=="POST":
        body_unicode = request.body.decode('utf-8')
        received_json_data = json.loads(body_unicode)
        email = received_json_data.get('email')
        password = received_json_data.get('password')
        cursor = connection.cursor()
        cursor.execute("select * from jiibs_backend_users WHERE jiibs_backend_users.email = '" + email + "' AND  jiibs_backend_users.password = '" + password+"'")
        if cursor.rowcount==0:
            return HttpResponse(json.dumps({"error":"Not Found"}),content_type="application/json")
        else:    
            cursor.execute("select * from jiibs_backend_users where jiibs_backend_users.email ='"+email+"' AND  jiibs_backend_users.password = '" + password+"'")
            dict_json=dictfetchall(cursor)
            return HttpResponse(json.dumps(dict_json),content_type="application/json")

