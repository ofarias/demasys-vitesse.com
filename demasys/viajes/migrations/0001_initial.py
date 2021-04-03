# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ruta'
        db.create_table(u'viajes_ruta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'viajes', ['Ruta'])

        # Adding M2M table for field casetas on 'Ruta'
        m2m_table_name = db.shorten_name(u'viajes_ruta_casetas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ruta', models.ForeignKey(orm[u'viajes.ruta'], null=False)),
            ('caseta', models.ForeignKey(orm[u'catalogos.caseta'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ruta_id', 'caseta_id'])

        # Adding model 'Viaje'
        db.create_table(u'viajes_viaje', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Departamento'])),
            ('economico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogos.Economico'])),
            ('operador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogos.Operador'])),
            ('ruta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['viajes.Ruta'])),
            ('referencia', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('contiene', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha_salida', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_conclusion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('flujo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflow.WorkflowActivity'], null=True, blank=True)),
        ))
        db.send_create_signal(u'viajes', ['Viaje'])


    def backwards(self, orm):
        # Deleting model 'Ruta'
        db.delete_table(u'viajes_ruta')

        # Removing M2M table for field casetas on 'Ruta'
        db.delete_table(db.shorten_name(u'viajes_ruta_casetas'))

        # Deleting model 'Viaje'
        db.delete_table(u'viajes_viaje')


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
            'autobus_3_ejes': ('django.db.models.fields.FloatField', [], {}),
            'autobus_4_ejes': ('django.db.models.fields.FloatField', [], {}),
            'autos': ('django.db.models.fields.FloatField', [], {}),
            'camion_2_ejes': ('django.db.models.fields.FloatField', [], {}),
            'camion_3_ejes': ('django.db.models.fields.FloatField', [], {}),
            'camion_4_ejes': ('django.db.models.fields.FloatField', [], {}),
            'camion_5_ejes': ('django.db.models.fields.FloatField', [], {}),
            'camion_6_ejes': ('django.db.models.fields.FloatField', [], {}),
            'camion_7_ejes': ('django.db.models.fields.FloatField', [], {}),
            'camion_8_ejes': ('django.db.models.fields.FloatField', [], {}),
            'camion_9_ejes': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {}),
            'motos': ('django.db.models.fields.FloatField', [], {}),
            'via': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'catalogos.economico': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Economico'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogos.ModeloEconomico']"}),
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
            'Meta': {'ordering': "['nombre']", 'object_name': 'Cliente'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        u'viajes.ruta': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Ruta'},
            'casetas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['catalogos.Caseta']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'viajes.viaje': {
            'Meta': {'object_name': 'Viaje'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'contiene': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Departamento']"}),
            'economico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogos.Economico']"}),
            'fecha_conclusion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_salida': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'flujo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workflow.WorkflowActivity']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogos.Operador']"}),
            'referencia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'ruta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['viajes.Ruta']"})
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