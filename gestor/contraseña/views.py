from django.shortcuts import HttpResponse
from django.http import JsonResponse
import pdb
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from contraseña.models import  usuario



# Create your views here.
def index(request):
    return HttpResponse("Porfavor, registre su usuario")

@csrf_exempt
def añadir(request):

    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    #pdb.set_trace()
    nuevo_usuario = usuario(usuario=body['usuario'] ,contraseña=body['contraseña'])
    nuevo_usuario.save()
    #body['usuario']
    
    response = {"Info": "correcta"}
    return JsonResponse(response)
