# coding: utf-8
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Q
from sepomex.models import Sepomex
import json
import operator
from django.template.context import RequestContext
from django.shortcuts import render_to_response

def direccion(request):
    busqueda = request.GET.get('term')
    resultados = Sepomex.objects.filter(Q(municipio__icontains=busqueda.strip()) | Q(ciudad__icontains=busqueda.strip())).values('id_asenta_cpcons', 'clave_estado', 'municipio', 'estado', 'ciudad').distinct()[0:10]
    
   
    data = []        
    for resultado in resultados:
        municipio = ''
        if resultado['ciudad'] != '' and resultado['ciudad'] != resultado['municipio']:
            municipio = '%s (%s)'%(resultado['municipio'], resultado['ciudad'])
        else:
            municipio = resultado['municipio']
        data.append({
                     'id':'%s-%s'%(resultado['clave_estado'], resultado['id_asenta_cpcons']), 
                     #'label': '%s, %s, %s, %s'%(resultado.asentamiento, resultado.municipio, resultado.estado, resultado.codigo),
                     #'value': resultado['id_asenta_cpcons'],
                     #'clave_estado': resultado.clave_estado,
                     #'clave_municipio': resultado.clave_municipio,
                     #'colonia': resultado.asentamiento,
                     'municipio': municipio,
                     'estado': resultado['estado'],
                     #'cp': resultado.codigo
        })
    
    return HttpResponse(json.dumps(data), 
                        content_type="application/json")
    
def direccion_recupera(request):
    ids = request.GET.get('ids')
    ids_array = ids.split(',')
    
    edos = []
    asenta = []
    for id in ids_array:
        e, a = id.split('-')
        edos.append(e)
        asenta.append(a)
        
    
    resultados = Sepomex.objects.filter(id_asenta_cpcons__in=asenta, clave_estado__in=edos).values('id_asenta_cpcons', 'clave_estado', 'municipio', 'estado', 'ciudad').distinct()
    data = []        
    for resultado in resultados:
        municipio = ''
        if resultado['ciudad'] != '' and resultado['ciudad'] != resultado['municipio']:
            municipio = '%s (%s)'%(resultado['municipio'], resultado['ciudad'])
        else:
            municipio = resultado['municipio']
        data.append({
                     'id':'%s-%s'%(resultado['clave_estado'], resultado['id_asenta_cpcons']),
                     #'label': '%s, %s, %s, %s'%(resultado.asentamiento, resultado.municipio, resultado.estado, resultado.codigo),
                     #'value': resultado['id_asenta_cpcons'],
                     #'clave_estado': resultado.clave_estado,
                     #'clave_municipio': resultado.clave_municipio,
                     #'colonia': resultado.asentamiento,
                     'municipio': municipio,
                     'estado': resultado['estado'],
                     #'cp': resultado.codigo
        })
    
    return HttpResponse(json.dumps(data), 
                        content_type="application/json")
    
def direccion_recupera_unico(request):
    ids = request.GET.get('ids')    
    
    e, a = ids.split('-')
    
    resultados = Sepomex.objects.filter(id_asenta_cpcons=a, clave_estado=e).values('id_asenta_cpcons', 'clave_estado', 'municipio', 'estado').distinct()
    data = {}      
    for resultado in resultados:
        data = {
                     'id':'%s-%s'%(resultado['clave_estado'], resultado['id_asenta_cpcons']),
                     #'label': '%s, %s, %s, %s'%(resultado.asentamiento, resultado.municipio, resultado.estado, resultado.codigo),
                     #'value': resultado['id_asenta_cpcons'],
                     #'clave_estado': resultado.clave_estado,
                     #'clave_municipio': resultado.clave_municipio,
                     #'colonia': resultado.asentamiento,
                     'municipio': resultado['municipio'],
                     'estado': resultado['estado'],
                     #'cp': resultado.codigo
        }
    
    return HttpResponse(json.dumps(data), 
                        content_type="application/json")    
    
@csrf_exempt
def estados(request):
    """
    Funcion que regresa los estados en formato json
    """
    estados = Sepomex.objects.values_list('estado', flat=True)\
                            .distinct()\
                            .order_by('estado')
                            
    return HttpResponse(json.dumps(list(estados)), 
                        content_type="application/json")
    
def get_by_cp(request, cp):
    """
    Funcion para recuperar colonias, municipio y estado por codigo postal
    """
    try: 
        estado = Sepomex.objects.values('estado').distinct('estado')\
                                .filter(codigo=cp)[0]['estado']
        municipio = Sepomex.objects.values('municipio').distinct('municipio')\
                                .filter(codigo=cp)[0]['municipio']
                                
        colonias = Sepomex.objects.values_list('asentamiento', flat=True)\
                                .distinct('asentamiento')\
                                .filter(codigo=cp)\
                                .order_by('asentamiento')
    except:
        estado = ''
        municipio = ''
        colonias = []
                            
    resultado = {'estado':estado, 'municipio':municipio, 'colonias':list(colonias)}
    
    return HttpResponse(json.dumps(resultado), 
                        content_type="application/json")
                        

@csrf_exempt
def colonias(request):
    """ Funcion para obtener las colonias del modelo de sepomex al recibir
    el id de la delegacion seleccionada en el combo de delegaciones de un
    formulario.
    
    """
    if request.is_ajax():
        if request.method == 'POST':
            # Consulta al modelo de sepomex filtrando por delegacion       
            asentamientos = Sepomex.objects.filter(
                        cve_cat_delegacion = request.POST['id_delegacion']
            ).order_by('d_asenta')
            results = []
            for asentamiento in asentamientos:
                asentamientos_dict = {'id':asentamiento.d_CP, 'label':asentamiento.d_asenta, 'value':asentamiento.d_asenta}
                results.append(asentamientos_dict)
            return HttpResponse(json.dumps(results),mimetype='application/json')

    else:
        message = "No XHR"
    
    return HttpResponse(message)

@csrf_exempt
def cp(request):
    """ Funcion para obtener el cp de una colonia
    """
    if request.is_ajax():
        if request.method == 'POST':
            # Consulta al modelo de sepomex filtrando por delegacion       
            queryset = Sepomex.objects.filter(
                        d_codigo = request.POST['id_cp']).order_by('D_mnpio')
            # Formatea los datos obtenidos a JSON
            json_serializer = serializers.get_serializer("json")()
            message = json_serializer.serialize(queryset, 
                                              ensure_ascii=False,
                                              fields=('cve_cat_delegacion',
                                                      'id',
                                                      'd_asenta'
                                                      )
                                              )
    else:
        message = "No XHR"
    
    return HttpResponse(message)

@csrf_exempt
def map(request, ):
    context = RequestContext(request,{ 
        
    })           
    return render_to_response('map.html', context)