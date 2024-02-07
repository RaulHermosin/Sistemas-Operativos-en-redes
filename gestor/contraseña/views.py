from django.shortcuts import HttpResponse
from django.http import JsonResponse
import pdb
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def index(request):
    return HttpResponse("Porfavor, registre su usuario")

@csrf_exempt
def añadir(request):
    
    #response={
    #    "Usuario": HttpResponse(usuario),
    #    "Contraseña": HttpResponse(contraseña)
    #}
    pdb.set_trace()
    string_body = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)
    body['usuario']
    response =  {}     
    return JsonResponse(response)