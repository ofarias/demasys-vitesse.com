def obtenerDatos(request):

    if request.method=='POST':

        form = repMensualForm(request.POST)
        
        if form.is_valid():         
            ####codigo para obtener los datos
            ##### Datos empleados ###
            ####codigo para obtener los datos
            ##### Datos empleados ###
            lista_Dir = Puestos.objects.filter(tipo = 1)
            lista_Adm = Puestos.objects.filter(tipo = 2)
            lista_Ope = Puestos.objects.filter(tipo = 3)
            lista_Man = Puestos.objects.filter(tipo = 4)
            lista_Cho = Puestos.objects.filter(tipo = 5)
            emppleado_alta = empleado.objects.filter(status = 1)
            nomdir=empleado.objects.filter(status =1, puesto = lista_Dir)
            nomadm=empleado.objects.filter(status = 1, puesto = lista_Adm)
            nomope=empleado.objects.filter(status = 1, puesto = lista_Ope)
            nomman=empleado.objects.filter(status =1, puesto = lista_Man)
            nomcho=empleado.objects.filter(status=1, puesto = lista_Cho)
            ntotal = emppleado_alta.count()
            nd = nomdir.count()
            na = nomadm.count()
            no = nomope.count()
            nm = nomman.count()
            nc = nomcho.count()     
            nt = nd + na + no + nm + nc
            print 'Estos son los Directivos: ' + str(nd)
            print 'Estos son los Administrativos: ' + str(na)
            print 'Estos son los Operativos: ' + str (no)
            print 'Estos son los de Mantenimiento: ' + str(nm)
            print 'Estos son los choferes: ' + str(nc)    
            print 'Este es el total de los empleados' + str (nt) +  "Estos son los totales activos" + str(ntotal)

            #### Datos de Movimientos ####
            mes = request.POST['mes']
            print 'Este es el mes que se selecciono:' + str(mes)
            if mes == 'Enero':
                inicial = '2016-01-01'
                final = '2016-01-30'
            elif mes == 'Febrero':
                inicial = '2016-02-01'
                final = '2016-02-28'
            elif mes == 'Marzo':
                inicial = '2016-03-01'
                final = '2016-03-31'
            elif mes == 'Abril':
                inicial = '2016-04-01'
                final = '2016-04-30'
            elif mes == 'Mayo':
                inicial = '2016-05-01'
                final = '2016-05-31'
            elif mes == 'Junio':
                inicial = '2016-06-01'
                final = '2016-06-30'
            elif mes == 'Julio':
                inicial = '2016-07-01'
                final = '2016-07-31'
            elif mes == 'Agosto':
                inicial = '2016-08-01'
                final = '2016-08-31'
            elif mes == 'Septiembre':
                inicial = '2016-09-01'
                final = '2016-09-30'
            elif mes == 'Octubre':
                inicial = '2016-10-01'
                final = '2016-10-31'
            elif mes == 'Novimebre':
                inicial = '2016-11-01'
                final = '2016-11-30'
            elif mes == 'Diciembre':
                inicial = '2016-12-01'
                final = '2016-12-01'

            filters={}
            filters_viaje={}
            if inicial and final:
                filters['fecha__range'] = (inicial, final)
                filters_viaje['fecha_salida__range'] = (inicial, final)

            print 'Inica la obtencion de datos.'
            #mov_alta2 = movimientos.objects.filter(fecha = mesdjango)
            #print mov_alta2.query
            mov_alta = movimientos.objects.filter(Q(tipo = 1) | Q(tipo = 3), **filters)
            mov_baja = movimientos.objects.filter(Q(tipo = 2)| Q(tipo = 7)|Q(tipo = 8), **filters)
            mov_alta_adm = movimientos.objects.filter(Q(tipo = 1)| Q(tipo = 2), empleado = nomadm, **filters)
            mov_alta_cho = movimientos.objects.filter(Q(tipo = 1)| Q(tipo = 2), empleado = nomope, **filters)
            print 'estos son los movimientos de Administracion ' + str(mov_alta_adm.count())
            print 'estos son los movimientos de Choferes' + str (mov_alta_cho.count())
            altas = mov_alta.count()
            bajas = mov_baja.count()
            total_movemp = int(altas) + int (bajas)
            print 'Altas = ' + str(altas)
            print 'Bajas = ' + str(bajas)
            print 'Total de Movimientos = ' + str(total_movemp)
            ################# Hasta aqui la informacion de la primer hoja #####################

            #########   Inicia las ventas Brutas y YTY POR CLIENTE ###########

            viajes= Viaje.objects.filter(**filters_viaje).aggregate(Sum('facturacion_flete'))
            print viajes
            fac_viajes = viajes.values()
            for val_fac in fac_viajes:
                fact_mes= val_fac
                print 'Este es el valor de la factura mensual' + str(fact_mes)

            clientes = Cliente.objects.all()

            for cli in clientes:
                clie = cli.id
                clien = cli.nombre
                viajes_1 = Viaje.objects.filter(cliente = clie, **filters_viaje).aggregate(Sum('facturacion_flete'))
                viajes_1 = viajes_1.values()
                for fac_cli in viajes_1:
                    cli_venta_mensual = fac_cli
                    print 'Este es el valor de la facturacion de ' + str(clien) + ' : ' + str(cli_venta_mensual)

            venta_samsung = Viaje.objects.filter(cliente = 1, **filters_viaje).aggregate(Sum('facturacion_flete'), Sum('facturacion_maniobra'), Sum('facturacion_desvio'),
                Sum('facturacion_reparto'), Sum('facturacion_ferri'), Sum('facturacion_ferri'), Sum('facturacion_otros'))
            print venta_samsung
            a= 0
            ventatot = 0
            for ven_sam in venta_samsung.values():
                i = 1
                a=a+i
                print a
                venta_sam = ven_sam                
                ventapar = ven_sam
                ventatot = ventatot + ventapar
                print venta_sam  
                print ventatot
            ##### Facturas Samsung 

            fact_sam = Viaje.objects.filter(cliente=1, **filters_viaje)
            for facturas in fact_sam:
                fact = facturas.factura
                fecha_viaje = facturas.fecha_salida 
                print 'Factura : ' + str(fact) + ' con fecha : ' + str(fecha_viaje) 

            #### Facturas LG 
            venta_lg = Viaje.objects.filter(cliente = 2, **filters_viaje).aggregate(Sum('facturacion_flete'), Sum('facturacion_maniobra'), Sum('facturacion_desvio'),
                Sum('facturacion_reparto'), Sum('facturacion_ferri'), Sum('facturacion_ferri'), Sum('facturacion_otros'))
            print venta_lg
            a= 0
            ventatot_lg = 0
            for ven_lg in venta_lg.values():
                venta_lg = ven_lg                
                ventatot_lg = ventatot + venta_lg
                print venta_lg 
                print ventatot_lg

            ##### Facturas LG 
            fact_lg = Viaje.objects.filter(cliente=1, **filters_viaje)
            for facturas in fact_lg:
                fact = facturas.factura
                fecha_viaje = facturas.fecha_salida 
                print 'Factura LG : ' + str(fact) + ' con fecha : ' + str(fecha_viaje) 
        ################   Termina Ventas LG y Samsung ##################
            ######## Inicia comparativo de ventas Mensuales Anuales########
            ##Enero###
            filters_enero15 ={}
            filters_enero={}
            inicial15 = '2015-01-01'
            final15 = '2015-01-30'
            filters_enero15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-01-30'
            filters_enero['fecha_salida__range']=(inicial, final) 
            ven_enero_15 = Viaje.objects.filter(cliente = 1, **filters_enero15).aggregate(Sum('facturacion_flete'))
            for ven0115 in ven_enero_15.values():
                Venta0115 = ven0115
                print 'Venta Samsung Enero 2015 : ' + str(Venta0115)
            ven_enero = Viaje.objects.filter(cliente=1, **filters_enero).aggregate(Sum('facturacion_flete'))
            for ven0116 in ven_enero.values():
                Venta0116= ven0116
                print 'Venta Samsung Enero 2016 : ' + str(Venta0116)
            difEnero = float 
            difEnero = ((float(ven0116)/float(ven0115)) -1) * 100
            difEne = int(ven0115)-int (ven0116)
            print difEne     
            print 'Diferencia Enero: ' + str(difEnero) 
            #### Febrero ####
            filters_feb15 ={}
            filters_feb={}
            inicial15 = '2015-02-01'
            final15 = '2015-02-28'
            filters_feb15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-02-01' 
            final= '2016-02-28'
            filters_feb['fecha_salida__range']=(inicial, final) 
            ven_feb_15 = Viaje.objects.filter(cliente = 1, **filters_feb15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_feb_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Febrero 2015 : ' + str(Venta0215)
            ven_feb = Viaje.objects.filter(cliente=1, **filters_feb).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_feb.values():
                Venta0216= ven0216
                print 'Venta Samsung Febrero 2016 : ' + str(Venta0216)
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Febrero: ' + str(difEnero) 
            ##### Marzo ########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-03-01'
            final15 = '2015-03-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-03-01' 
            final= '2016-03-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Marzo 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Samsung Marzo 2016 : ' + str(Venta0216)
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Marzo: ' + str(difEnero) 
            ##### Abril ########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-04-01'
            final15 = '2015-04-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-04-01' 
            final= '2016-04-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Abril 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Samsung Abril 2016 : ' + str(Venta0216)
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Abril: ' + str(difEnero) 
            ######### Mayo##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-05-01'
            final15 = '2015-05-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-05-01' 
            final= '2016-05-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Mayo 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Samsung Mayo 2016 : ' + str(Venta0216)
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Mayo: ' + str(difEnero)
            ######### Junio ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-06-01'
            final15 = '2015-06-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-06-01' 
            final= '2016-06-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Junio 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Samsung Junio 2016 : ' + str(Venta0216)
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Junio: ' + str(difEnero)  
            ######### Julio##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-07-01'
            final15 = '2015-07-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-07-01' 
            final= '2016-07-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Julio 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Samsung Julio 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Julio: ' + str(difEnero) 
             ######### Agosto ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-08-01'
            final15 = '2015-08-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-08-01' 
            final= '2016-08-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Agosto 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Samsung Agosto 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Agosto: ' + str(difEnero) 
             ######### Septiembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-09-01'
            final15 = '2015-09-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-09-01' 
            final= '2016-09-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Septiembre 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Samsung Septiembre 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Septiembre: ' + str(difEnero) 
            ######### Octubre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-10-01'
            final15 = '2015-10-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-10-01' 
            final= '2016-10-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Octubre 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Samsung Octubre 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Octubre: ' + str(difEnero) 
             ######### Noviembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-11-01'
            final15 = '2015-11-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-11-01' 
            final= '2016-11-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Noviembre 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Samsung Noviembre 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Novimebre: ' + str(difEnero) 
            ######### Diciembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-12-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-12-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Diciembre 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Samsung Diciembre 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Diciembre: ' + str(difEnero)
            ######### 2015 ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-01-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Anual: ' + str(difEnero)  
        ################   Termina Ventas LG y LG ##################
            ######## Inicia comparativo de ventas Mensuales Anuales########
            ##Enero###
            filters_enero15 ={}
            filters_enero={}
            inicial15 = '2015-01-01'
            final15 = '2015-01-30'
            filters_enero15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-01-30'
            filters_enero['fecha_salida__range']=(inicial, final) 
            ven_enero_15 = Viaje.objects.filter(cliente = 2, **filters_enero15).aggregate(Sum('facturacion_flete'))
            for ven0115 in ven_enero_15.values():
                Venta0115 = ven0115
                print 'Venta LG Enero 2015 : ' + str(Venta0115)
            ven_enero = Viaje.objects.filter(cliente=2, **filters_enero).aggregate(Sum('facturacion_flete'))
            for ven0116 in ven_enero.values():
                Venta0116= ven0116
                print 'Venta LG Enero 2016 : ' + str(Venta0116)
            difEnero = float 
            difEnero = ((float(ven0116)/float(ven0115)) -1) * 100
            difEne = int(ven0115)-int (ven0116)
            print difEne     
            print 'Diferencia Enero: ' + str(difEnero) 
            #### Febrero ####
            filters_feb15 ={}
            filters_feb={}
            inicial15 = '2015-02-01'
            final15 = '2015-02-28'
            filters_feb15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-02-01' 
            final= '2016-02-28'
            filters_feb['fecha_salida__range']=(inicial, final) 
            ven_feb_15 = Viaje.objects.filter(cliente = 2, **filters_feb15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_feb_15.values():
                Venta0215 = ven0215
                print 'Venta LG Febrero 2015 : ' + str(Venta0215)
            ven_feb = Viaje.objects.filter(cliente=2, **filters_feb).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_feb.values():
                Venta0216= ven0216
                print 'Venta LG Febrero 2016 : ' + str(Venta0216)
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Febrero: ' + str(difEnero) 
            ##### Marzo ########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-03-01'
            final15 = '2015-03-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-03-01' 
            final= '2016-03-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Marzo 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Marzo 2016 : ' + str(Venta0216)
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Marzo: ' + str(difEnero) 
            ##### Abril ########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-04-01'
            final15 = '2015-04-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-04-01' 
            final= '2016-04-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Abril 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Abril 2016 : ' + str(Venta0216)
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Abril: ' + str(difEnero) 
            ######### Mayo##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-05-01'
            final15 = '2015-05-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-05-01' 
            final= '2016-05-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Mayo 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Mayo 2016 : ' + str(Venta0216)
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Mayo: ' + str(difEnero)
            ######### Junio ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-06-01'
            final15 = '2015-06-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-06-01' 
            final= '2016-06-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Junio 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Junio 2016 : ' + str(Venta0216)
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Junio: ' + str(difEnero)  
            ######### Julio##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-07-01'
            final15 = '2015-07-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-07-01' 
            final= '2016-07-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Julio 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Julio 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Julio: ' + str(difEnero) 
             ######### Agosto ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-08-01'
            final15 = '2015-08-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-08-01' 
            final= '2016-08-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Agosto 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Agosto 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Agosto: ' + str(difEnero) 
             ######### Septiembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-09-01'
            final15 = '2015-09-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-09-01' 
            final= '2016-09-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Septiembre 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Septiembre 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Septiembre: ' + str(difEnero) 
            ######### Octubre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-10-01'
            final15 = '2015-10-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-10-01' 
            final= '2016-10-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Octubre 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Octubre 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Octubre: ' + str(difEnero) 
             ######### Noviembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-11-01'
            final15 = '2015-11-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-11-01' 
            final= '2016-11-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Noviembre 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Noviembre 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Novimebre: ' + str(difEnero) 
            ######### Diciembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-12-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-12-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Diciembre 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Diciembre 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Diciembre: ' + str(difEnero)
            ######### 2015 ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-01-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Anual: ' + str(difEnero)
            #############  Venta Bruta ##############
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-01-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(**filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Bruta : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(**filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Bruta : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Anual: ' + str(difEnero)
            ############# Ventas Netas ###############
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-01-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(**filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Neta : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(**filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Neta : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Anual: ' + str(difEnero)


        else: 
            messages.error(request,'Ha ocurrido un error')
    else:
        form=repMensualForm()
    context = RequestContext(request,{
        'form':form,
        'action':'Obtener',
        })
    return render_to_response('generaRepMensual.html', context)