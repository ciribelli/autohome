from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.template import Template, Context
import math
from random import *
from controleambiente.models import Local, Ambiente, ArcondState
import json
from django.core import serializers


def teste(request):
    now = str(datetime.datetime.now()) + "  " + "Otavio"
    return HttpResponse(now)


def leArquivo(sensor):
    file = open('/home/pi/Projetos/'+sensor, 'r')
    valorLido = file.read()
    indice = (valorLido).index(';')
    temperatura = valorLido[0:indice]
    umidade = valorLido[indice+1:]
    return (temperatura, umidade)


def home(request):
    variavel =  "variavel passada"
    #arquivo = (leArquivo("sensor_23"))
    temp1 = 11.1
    umid1 = 22.2
    #arquivo = (leArquivo("sensor_24"))
    temp2 = 50.0#arquivo[0]
    umid2 = 17.7#arquivo[1]
    locals = []
    locals = json.dumps(serializers.serialize('json', Local.objects.all()))

    ambiente = []
    
   
    try:
        ambiente = json.dumps(serializers.serialize('json', Ambiente.objects.order_by('-id')[:100]))
    except Exception as ex:
        ambiente = 'deupau20' + str(ex)


    #arcond = json.dumps(serializers.serialize('json', ArcondState.objects.all().last()))
    arcond1 = ArcondState.objects.filter(local = 0).last()
    arcond2 = ArcondState.objects.filter(local = 1).last()
    return render(request, 'controleambiente/pessoal.html', {'temp1': temp1, 'umid1': umid1, 'temp2': temp2, 'umid2': umid2, 'ambiente': ambiente, 'arcond1': arcond1, 'arcond2': arcond2})


#def home(request):
    #return render(request, 'controleambiente/pessoal.html',)
