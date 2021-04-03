from django.db import models

TIPOS = (
	(1,'Fisica'),
	(2,'Moral'),
)

TIPO_PROD = (
	(1,'Servicio'),
	(2,'Producto'),
)

class Benefi (models.Model):
	tipo = models.IntegerField(choices = TIPOS, null = False)
	razon_social = models.CharField(max_length = 150, null = True) 
	nombre = models.CharField(max_length = 150, null = False)
	a_paterno = models.CharField (max_length= 50, null = True)
	a_materno = models.CharField (max_length = 50, null = True)
	calle = models.CharField(max_length = 100, null = True)
	no_ext = models.CharField(max_length = 11, null = True)
	no_int = models.CharField(max_length = 11, null = True)
	producto = models.IntegerField(choices = TIPO_PROD, null = True)
	col = models.CharField(max_length= 100, null = True)
	mun_est = models.CharField(max_length = 100, null = True)
	cp = models.IntegerField(null = True)
	no_cta = models.CharField(max_length = 20, null = True, unique = True)
	ban = models.CharField(max_length = 60, null = True)
	clabe = models.CharField(max_length = 20, null = True, unique = True)


	def __unicode__(self):
		return u'%s %s %s' % (self.nombre, self.a_paterno, self.a_materno) 
	
	class Meta:
		ordering = ["nombre"]

# Create your models here.
