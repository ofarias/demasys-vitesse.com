from django.db import models

MESES = (
    ('1', 'Enero'),
    ('2', 'Febrero'),
    ('3', 'Marzo'),
    ('4', 'Abril'),
    ('5', 'Mayo'),
    ('6', 'Junio'),
    ('7', 'Julio'),
    ('8', 'Agosto'),
    ('Septiembre', 'Septiembre'),
    ('Octubre', 'Octubre'),
    ('Noviembre', 'Noviembre'),
    ('Diciembre', 'Diciembre'),
)

CLIENTE = (
    ('Samsung', 'Samsung'),
    ('LG', 'LG'),
)

class ing_egre(models.Model):  ### Hoja 1 
    mes = models.CharField (choices=MESES, max_length = 20, null = True)
    egresoChoferes = models.IntegerField(blank=False, null = False)
    ingresoChoferes = models.IntegerField(blank=False, null = False)
    egresoAdmin = models.IntegerField(blank=False, null = False)
    ingresoAdmin = models.IntegerField(blank=False, null = False)
    directivo = models.IntegerField(blank=False, null = False)
    administrativo = models.IntegerField(blank=False, null = False)
    operaciones = models.IntegerField(blank=False, null = False)
    mantenimiento = models.IntegerField(blank=False, null = False)
    choferes = models.IntegerField(blank=False, null = False)
    total = models.IntegerField(blank=False, null = False)
    mov = models.IntegerField(blank=False, null = False)
    porcentaje = models.IntegerField(blank=False, null = False)
    texto_nom1 = models.TextField(null =True)
    texto_nom2 = models.TextField(null = True)
    texto_nom3 = models.TextField(null= True)
    texto_nom4 = models.TextField(null = True)
    texto_nom5 = models.TextField(null = True)
    org_dir = models.CharField(max_length=100, null = True) ### Direccion
    org_jft = models.CharField(max_length=100, null = True) #### Taller
    org_jfa = models.CharField(max_length=100, null = True)  ### Administrativo
    org_f = models.CharField(max_length=100, null = True)   #### Facturacion
    org_cli = models.CharField(max_length=100, null = True) #### Logisica Inversa
    org_clg = models.CharField(max_length=100, null = True) ### Coordinador LG 
    org_jfo = models.CharField(max_length=100, null = True) #### Jefe de Operaciones.
    org_choferes = models.CharField(max_length=100, null = True)  ###Choferes.
    texto_dist1 = models.CharField(max_length=100, null = True)
    texto_dist2 = models.CharField(max_length=100, null = True)
    texto_dist3 = models.CharField(max_length=100, null = True)
    texto_dist4 = models.CharField(max_length=100, null = True)
    texto_dist5 = models.CharField(max_length=100, null = True)
    

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]

class nomina(models.Model):
    idRep = models.ForeignKey(ing_egre, db_column='idRep')
    mes = models.CharField (choices=MESES, max_length = 20, null = True)
    operador = models.CharField (max_length = 20, null = True)
    administrativo = models.CharField (max_length = 20, null = True)
    total = models.CharField (max_length = 20, null = True)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]

class venta_bruta(models.Model):
    idRep = models.ForeignKey(ing_egre, db_column='idRep')
    mes = models.CharField (choices=MESES, max_length = 20, null = True)
    cliente = models.CharField (choices=CLIENTE, max_length = 20, null = True)
    actual= models.CharField (max_length = 30, null = True)
    anterior = models.CharField (max_length = 30, null = True)
    deocre = models.CharField (max_length = 30, null = True)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]

class venta_neta(models.Model):
    idRep = models.ForeignKey(ing_egre, db_column='idRep')
    mes = models.CharField (choices=MESES, max_length = 20, null = True)
    cliente = models.CharField (choices=CLIENTE, max_length = 20, null = True)
    actual= models.CharField (max_length = 30, null = True)
    anterior = models.CharField (max_length = 30, null = True)
    deocre = models.CharField (max_length = 30, null = True)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]

class infoMensual(models.Model):
    ### Hoja 3 ####
    mes= models.CharField(max_length=20, null = False)
    egresoChoferes=models.IntegerField(null = False)
    egresoAdmin=models.IntegerField(null = False)
    ingresoChoferes=models.IntegerField(null = False)
    ingresoAdmin=models.IntegerField(null = False)
    directivo=models.IntegerField(null = False)
    administracion=models.IntegerField(null = False)
    operaciones=models.IntegerField(null = False)
    mantenimiento=models.IntegerField(null = False)
    choferes=models.IntegerField(null = False)
    totalPersonal=models.IntegerField(null = False)
    rotacion=models.IntegerField(null = False)
    ### Hoja  4 ####
    nomina_1_15=models.IntegerField(null=False)
    nomina_1_16=models.IntegerField(null=False)
    nomina_1_17=models.IntegerField(null=False)
    nomina_2_15=models.IntegerField(null=False)
    nomina_2_16=models.IntegerField(null=False)
    nomina_2_17=models.IntegerField(null=False)
    nomina_3_15=models.IntegerField(null=False)
    nomina_3_16=models.IntegerField(null=False)
    nomina_3_17=models.IntegerField(null=False)
    nomina_4_15=models.IntegerField(null=False)
    nomina_4_16=models.IntegerField(null=False)
    nomina_4_17=models.IntegerField(null=False)
    nomina_5_15=models.IntegerField(null=False)
    nomina_5_16=models.IntegerField(null=False)
    nomina_5_17=models.IntegerField(null=False)
    nomina_6_15=models.IntegerField(null=False)
    nomina_6_16=models.IntegerField(null=False)
    nomina_6_17=models.IntegerField(null=False)
    nomina_7_15=models.IntegerField(null=False)
    nomina_7_16=models.IntegerField(null=False)
    nomina_7_17=models.IntegerField(null=False)
    nomina_8_15=models.IntegerField(null=False)
    nomina_8_16=models.IntegerField(null=False)
    nomina_8_17=models.IntegerField(null=False)
    nomina_9_15=models.IntegerField(null=False)
    nomina_9_16=models.IntegerField(null=False)
    nomina_9_17=models.IntegerField(null=False)
    nomina_10_15=models.IntegerField(null=False)
    nomina_10_16=models.IntegerField(null=False)
    nomina_10_17=models.IntegerField(null=False)
    nomina_11_15=models.IntegerField(null=False)
    nomina_11_16=models.IntegerField(null=False)
    nomina_11_17=models.IntegerField(null=False)
    nomina_12_15=models.IntegerField(null=False)
    nomina_12_16=models.IntegerField(null=False)
    nomina_12_17=models.IntegerField(null=False)
    text_nom1=models.CharField(max_length=255, null = True)
    text_nom2=models.CharField(max_length=255, null = True)
    text_nom3=models.CharField(max_length=255, null = True)
    text_nom4=models.CharField(max_length=255, null = True)
    text_nom5=models.CharField(max_length=255, null = True)
    ###### Texto Nomina #######
    text_nom6=models.CharField(max_length=255, null = True)
    text_nom7=models.CharField(max_length=255, null = True)
    text_nom8=models.CharField(max_length=255, null = True)
    text_nom9=models.CharField(max_length=255, null = True)
    text_nom10=models.CharField(max_length=255, null = True)
    ###### Organigrama ########
    org_dir = models.CharField(max_length=100, null = True) ### Direccion
    org_jft = models.CharField(max_length=100, null = True) #### Taller
    org_jfa = models.CharField(max_length=100, null = True)  ### Administrativo
    org_f = models.CharField(max_length=100, null = True)   #### Facturacion
    org_cli = models.CharField(max_length=100, null = True) #### Logisica Inversa
    org_clg = models.CharField(max_length=100, null = True) ### Coordinador LG 
    org_jfo = models.CharField(max_length=100, null = True) #### Jefe de Operaciones.
    org_choferes = models.CharField(max_length=100, null = True)  ###Choferes.
    ####### Texto de Niminas 2 ########
    texto_dist1 = models.CharField(max_length=100, null = True)
    texto_dist2 = models.CharField(max_length=100, null = True)
    texto_dist3 = models.CharField(max_length=100, null = True)
    texto_dist4 = models.CharField(max_length=100, null = True)
    texto_dist5 = models.CharField(max_length=100, null = True)



    def __unicode__(self):
        return self.mes
    class Meta:
        ordering = ["mes"]            



