@login_required
def documentosEmpleado(request, empleado_id):
    archivos = []
    if request.method == 'POST':
        #formDoc = ArchivosForm(initial={'idsolicitante':empleado_id})
        #archivo = Archivos.objects.get()
        formDoc = ArchivosForm(request.POST, request.FILES)
        formPost = ArchivosForm(request.POST)
        #print formDoc
        
        if formPost.is_valid():
            print 'Es valido'

            #print formDoc.cleaned_data['idsolicitante']
            #print request.POST['idsolicitante']
            #print formDoc.cleaned_data['idDoc']
            #print formDoc.cleaned_data['nombreDoc']
            #emple=formDoc.cleaned_data['idsolicitante']
            #emp=empleado.objects.filter(id=emple)
            #print emple
            #empleado=request.POST['idsolicitante']
            #print empleado

            formPost.save(commit=False)
            num=formPost.nombreDoc
            print 'este es el numero: ' + num



        

            #try:
            #    tipoDoc = Catdoc.objects.get(nombreDoc = formDoc.cleaned_data['idDoc'])
            #    print tipoDoc.nombreDoc
            #    ##archivo = Archivos.objects.get(idsolicitante = formDoc.cleaned_data['idsolicitante'], idDoc = tipoDoc.pk)
            #    archivo = Archivos.objects.get(idsolicitante = empleado, idDoc = tipoDoc.pk)
            #    print 'Este es el archivo ' + archivo
            #    print 'eliminando archivo anterior' + str(archivo.nombreDoc)
            #    ruta = settings.MEDIA_ROOT + str(archivo.nombreDoc)
            #    os.remove(ruta)
            #    formDoc = ArchivosForm(request.POST, request.FILES, instance=archivo)
                #formDoc.save()
            #    messages.success(request, u'Archivos actualizados exitosamente')
            #except Exception:

                #formDoc.save()
            #    messages.success(request, u'Archivos cargados exitosamente')


    else:
        formDoc = ArchivosForm(initial={'idsolicitante':empleado_id})
        print 'NO Es valido'


    #print 'este es el idsol: '+ empleado

    #archivos = Archivos.objects.filter(idsolicitante = empleado.objects.get(pk=empleado_id))
    archivos = Archivos.objects.filter(idsolicitante= empleado)
    context = RequestContext(request,{
        'formDoc':formDoc,
        'action': 'Editar',
        'archivos': archivos,
        'empleadoId' : empleado_id
    })
    return render_to_response('empleados_doc.html', context)