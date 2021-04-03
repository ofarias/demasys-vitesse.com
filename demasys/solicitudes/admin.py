from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
	
	def get_readonly_display(self, request, obj=None):
		if obj:
			return ['solicitante']
		else:
			return []


# Register your models here.
