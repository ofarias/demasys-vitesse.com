# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Viaje.facturacion_forma_pago'
        db.add_column(u'viajes_viaje', 'facturacion_forma_pago',
                      self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Viaje.facturacion_banco'
        db.add_column(u'viajes_viaje', 'facturacion_banco',
                      self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Viaje.facturacion_documento'
        db.add_column(u'viajes_viaje', 'facturacion_documento',
                      self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Viaje.facturacion_casetas'
        db.add_column(u'viajes_viaje', 'facturacion_casetas',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Viaje.facturacion_forma_pago'
        db.delete_column(u'viajes_viaje', 'facturacion_forma_pago')

        # Deleting field 'Viaje.facturacion_banco'
        db.delete_column(u'viajes_viaje', 'facturacion_banco')

        # Deleting field 'Viaje.facturacion_documento'
        db.delete_column(u'viajes_viaje', 'facturacion_documento')

        # Deleting field 'Viaje.facturacion_casetas'
        db.delete_column(u'viajes_viaje', 'facturacion_casetas')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'catalogos.caseta': {
            'Meta': {'ordering': "['via']", 'object_name': 'Caseta'},
            'autobus_2_ejes': ('django.db.models.fields.FloatField', [], {}),
            'autos': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'via': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'catalogos.economico': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Economico'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogos.ModeloEconomico']"}),
            'pasa_como': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'placas': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'catalogos.modeloeconomico': {
            'Meta': {'ordering': "['modelo']", 'object_name': 'ModeloEconomico'},
            'capacidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'catalogos.operador': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Operador'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'clientes.cliente': {
            'Meta': {'ordering': "['nombre_corto']", 'object_name': 'Cliente'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'facturacion_calle': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'facturacion_clave_municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'facturacion_colonia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'facturacion_cp': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'facturacion_numero': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'recoleccion_calle': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'recoleccion_clave_municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recoleccion_colonia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'recoleccion_cp': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'recoleccion_numero': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'})
        },
        u'clientes.departamento': {
            'Meta': {'ordering': "['departamento']", 'object_name': 'Departamento'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'departamento': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'viajes.comprobante': {
            'Meta': {'object_name': 'Comprobante'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'gasto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['viajes.Gasto']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'viajes.destino': {
            'Meta': {'object_name': 'Destino'},
            'comprobante_entrega': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'destino_calle': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'destino_clave_municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'destino_colonia': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'destino_cp': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'destino_nombre': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'destino_numero': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fecha_entrega': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'viaje': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['viajes.Viaje']"})
        },
        u'viajes.gasto': {
            'Meta': {'object_name': 'Gasto'},
            'calculado': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'comentarios': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'concepto': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pagado_contabilidad': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'pagado_operaciones': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'viaje': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['viajes.Viaje']"})
        },
        u'viajes.ruta': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Ruta'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'casetas_regreso': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'regreso'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['catalogos.Caseta']"}),
            'casetas_salida': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'salida'", 'symmetrical': 'False', 'to': u"orm['catalogos.Caseta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'viajes.viaje': {
            'Meta': {'ordering': "['-fecha_salida']", 'object_name': 'Viaje'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'contiene': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Departamento']"}),
            'economico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogos.Economico']"}),
            'factura': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'facturacion_banco': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'facturacion_casetas': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'facturacion_desvio': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'facturacion_documento': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'facturacion_ferri': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'facturacion_flete': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'facturacion_forma_pago': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'facturacion_maniobra': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'facturacion_otros': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'facturacion_reparto': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'fecha_salida': ('django.db.models.fields.DateField', [], {}),
            'flujo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workflow.WorkflowActivity']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'operador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogos.Operador']"}),
            'origen_calle': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'origen_clave_municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'origen_colonia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'origen_cp': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'origen_numero': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'referencia': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'ruta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['viajes.Ruta']"}),
            'tipo_ruta': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        u'viajes.viajestatus': {
            'Meta': {'object_name': 'ViajeStatus', 'db_table': "'workflow_stats'", 'managed': 'False'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'days': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workflow.State']"}),
            'workflowactivity': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['viajes.Viaje']", 'to_field': "'flujo'", 'unique': 'True', 'primary_key': 'True'})
        },
        u'workflow.role': {
            'Meta': {'ordering': "['name']", 'object_name': 'Role'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'workflow.state': {
            'Meta': {'ordering': "['-is_start_state', 'is_end_state']", 'object_name': 'State'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'estimation_unit': ('django.db.models.fields.IntegerField', [], {'default': '86400'}),
            'estimation_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_end_state': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_start_state': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['workflow.Role']", 'symmetrical': 'False', 'blank': 'True'}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'states'", 'to': u"orm['workflow.Workflow']"})
        },
        u'workflow.workflow': {
            'Meta': {'ordering': "['status', 'name']", 'object_name': 'Workflow'},
            'cloned_from': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workflow.Workflow']", 'null': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'workflow.workflowactivity': {
            'Meta': {'ordering': "['-completed_on', '-created_on']", 'object_name': 'WorkflowActivity'},
            'completed_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workflow.Workflow']"})
        }
    }

    complete_apps = ['viajes']