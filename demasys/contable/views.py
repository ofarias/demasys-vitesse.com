from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from django.views.decorators.csrf import csrf_exempt
from contable.models import Partidas, Movimientos, Area
from contable.forms import MovimientosForm
from django.contrib import messages
from django.db.models import Sum

# Create your views here.


@csrf_exempt
@login_required
def registrar(request):

    pila = []
    pilaO = []
    for x in range(1,5):
        saldoC = saldoPartidaXArea(x,2)
        pila.append(saldoC)
        saldoO = saldoPartidaXArea(x,3)
        pilaO.append(saldoO)

    saldoTransferencia = pila.pop()
    pila.pop()
    saldoVale = pila.pop()
    saldoEfectivo = pila.pop()

    saldoTO = pilaO.pop()
    pilaO.pop()
    saldoVO = pilaO.pop()
    saldoEO = pilaO.pop()

    current_user = request.user
    if request.method=='POST':
        idPartida = request.POST['partida']
        monto = request.POST['monto']
        idArea = request.POST['areas']
        movForm = MovimientosForm(request.GET)
        if request.POST['monto'] and request.POST['partida'] and request.POST['areas']:
            saldo_partida_act = saldoPartidaXArea(idPartida, idArea)
            movimiento = Movimientos(idPartida=Partidas.objects.get(id = idPartida), idArea = Area.objects.get(id = idArea), id_auth_user=current_user, importe=monto, tipo='A', montoPartida=saldo_partida_act)
            movimiento.save()

            if idArea == '3':
                saldo_partida_conta = saldoPartidaXArea(idPartida, 2)
                afectaConta = Movimientos(idPartida=Partidas.objects.get(id = idPartida), idArea = Area.objects.get(id = 2), id_auth_user=current_user, importe=monto, tipo='C', montoPartida=saldo_partida_conta)
                afectaConta.save()
            pila = []
            pilaO = []
            for x in range(1,5):
                saldoC = saldoPartidaXArea(x,2)
                pila.append(saldoC)
                saldoO = saldoPartidaXArea(x,3)
                pilaO.append(saldoO)

            saldoTransferencia = pila.pop()
            pila.pop()
            saldoVale = pila.pop()
            saldoEfectivo = pila.pop()

            saldoTO = pilaO.pop()
            pilaO.pop()
            saldoVO = pilaO.pop()
            saldoEO = pilaO.pop()
            messages.success(request, 'El saldo se agrego correctamente')
            context = RequestContext (request, {
                'saldoEfectivo':saldoEfectivo,
                'saldoVale':saldoVale,
                'saldoTransferencia':saldoTransferencia,
                'saldoEO':saldoEO,
                'saldoVO':saldoVO,
                'saldoTO':saldoTO,
                'movForm':movForm
            })
            return render_to_response ('asignarSaldo.html', context)
        else:
            messages.error(request, 'Ha ocurrido algun error, favor de revisar los datos')
    else:
        partidas = Partidas.objects.all()
        movForm = MovimientosForm(request.GET)
    context = RequestContext (request, {
        'saldoEfectivo':saldoEfectivo,
        'saldoVale':saldoVale,
        'saldoTransferencia':saldoTransferencia,
        'saldoEO':saldoEO,
        'saldoVO':saldoVO,
        'saldoTO':saldoTO,
        'movForm':movForm
    })
    return render_to_response ('asignarSaldo.html', context)

def saldoPartidaXArea(idPartida, idArea):
    sal = Movimientos.objects.filter(tipo ='A', idPartida = idPartida, idArea = idArea).aggregate(importe__sum = Sum('importe'))
    abonoEfectivoC = sal['importe__sum']
    #print abonoEfectivoC
    if abonoEfectivoC is None:
        abonoEfectivoC = 0
    cargoE = Movimientos.objects.filter(tipo ='C', idPartida = idPartida, idArea = idArea).aggregate(importe__sum = Sum('importe'))
    cargoEfectivo = cargoE['importe__sum']
    #print cargoEfectivo
    if cargoEfectivo is None:
        cargoEfectivo = 0
    nSaldo = abonoEfectivoC - cargoEfectivo
    return nSaldo