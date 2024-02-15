from django.shortcuts import HttpResponse
from django.http import JsonResponse
import pdb
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from biblioteca.models import libro
from django.views.decorators.csrf import csrf_exempt
from django.db import models



# Create your views here.
def index(request):
    return HttpResponse("Porfavor, registre su usuario")




@csrf_exempt
def crearlibro(request):

    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    #pdb.set_trace()
    nuevo_libro = libro(libro=body['libro'], pagina=body['pagina'])
    nuevo_libro.save()
    
    response = {"Info": "correcta"}
    return JsonResponse(response)   




@csrf_exempt
def verlibro(request):
    libros = list(libro.objects.values())
    return JsonResponse(libros, safe=False)



@csrf_exempt
def borrarlibro(request):

    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    #pdb.set_trace()
    borrar_libro = libro.objects.get(id=body['id'])
    borrar_libro.delete()
    
    response = {"Info": "correcta"}
    return JsonResponse(response)

