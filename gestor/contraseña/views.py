from django.shortcuts import HttpResponse
from django.http import JsonResponse
import pdb
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from contraseña.models import  usuario
from django.views.decorators.csrf import csrf_exempt
from django.db import models

# Create your views here.
def index(request):
    return HttpResponse("Porfavor, registre su usuario")

@csrf_exempt
def añadir(request):

    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    #pdb.set_trace()
    nuevo_usuario = usuario(usuario=body['usuario'], contraseña=body['contraseña'])
    nuevo_usuario.save()
    #body['usuario']
    
    response = {"Info": "correcta"}
    return JsonResponse(response)

@csrf_exempt
def mi_vista_sin_proteccion_csrf(request):
    # Tu lógica de vista aquí
    return JsonResponse("Esta vista no tiene protección CSRF.")
@csrf_exempt
def borrar(request):

    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    #pdb.set_trace()
    borrar_usuario = usuario.objects.get(id=body['id'])
    borrar_usuario.delete()
    
    response = {"Info": "correcta"}
    return JsonResponse(response)

@csrf_exempt
def actualizar(request):

    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    #pdb.set_trace()
    actualizar_contra = usuario.objects.get(id=body['id'], usuario=body['usuario'], contraseña = body['contraseña'])
    actualizar_contra.update()
    
    response = {"Info": "correcta"}
    return JsonResponse(response)