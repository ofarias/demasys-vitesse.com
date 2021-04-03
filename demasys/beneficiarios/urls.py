from django.conf.urls import patterns

urlpatterns = patterns ('beneficiarios.views',
		(r'^$','index'),
		(r'^add/$','agregar'),
		(r'^edit/(?P<benefi_id>\d+)/$','editar'),
)
