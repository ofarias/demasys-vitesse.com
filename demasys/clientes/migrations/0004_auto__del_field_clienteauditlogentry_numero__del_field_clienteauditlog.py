# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ClienteAuditLogEntry.numero'
        db.delete_column(u'clientes_clienteauditlogentry', 'numero')

        # Deleting field 'ClienteAuditLogEntry.estado'
        db.delete_column(u'clientes_clienteauditlogentry', 'estado')

        # Deleting field 'ClienteAuditLogEntry.municipio'
        db.delete_column(u'clientes_clienteauditlogentry', 'municipio')

        # Deleting field 'ClienteAuditLogEntry.colonia'
        db.delete_column(u'clientes_clienteauditlogentry', 'colonia')

        # Deleting field 'ClienteAuditLogEntry.calle'
        db.delete_column(u'clientes_clienteauditlogentry', 'calle')

        # Adding field 'ClienteAuditLogEntry.facturacion_clave_municipio'
        db.add_column(u'clientes_clienteauditlogentry', 'facturacion_clave_municipio',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'ClienteAuditLogEntry.facturacion_colonia'
        db.add_column(u'clientes_clienteauditlogentry', 'facturacion_colonia',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'ClienteAuditLogEntry.facturacion_calle'
        db.add_column(u'clientes_clienteauditlogentry', 'facturacion_calle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'ClienteAuditLogEntry.facturacion_numero'
        db.add_column(u'clientes_clienteauditlogentry', 'facturacion_numero',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'ClienteAuditLogEntry.facturacion_cp'
        db.add_column(u'clientes_clienteauditlogentry', 'facturacion_cp',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ClienteAuditLogEntry.recoleccion_clave_municipio'
        db.add_column(u'clientes_clienteauditlogentry', 'recoleccion_clave_municipio',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'ClienteAuditLogEntry.recoleccion_colonia'
        db.add_column(u'clientes_clienteauditlogentry', 'recoleccion_colonia',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'ClienteAuditLogEntry.recoleccion_calle'
        db.add_column(u'clientes_clienteauditlogentry', 'recoleccion_calle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'ClienteAuditLogEntry.recoleccion_numero'
        db.add_column(u'clientes_clienteauditlogentry', 'recoleccion_numero',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'ClienteAuditLogEntry.recoleccion_cp'
        db.add_column(u'clientes_clienteauditlogentry', 'recoleccion_cp',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Cliente.calle'
        db.delete_column(u'clientes_cliente', 'calle')

        # Deleting field 'Cliente.numero'
        db.delete_column(u'clientes_cliente', 'numero')

        # Deleting field 'Cliente.colonia'
        db.delete_column(u'clientes_cliente', 'colonia')

        # Deleting field 'Cliente.estado'
        db.delete_column(u'clientes_cliente', 'estado')

        # Deleting field 'Cliente.municipio'
        db.delete_column(u'clientes_cliente', 'municipio')

        # Adding field 'Cliente.facturacion_clave_municipio'
        db.add_column(u'clientes_cliente', 'facturacion_clave_municipio',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Cliente.facturacion_colonia'
        db.add_column(u'clientes_cliente', 'facturacion_colonia',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Cliente.facturacion_calle'
        db.add_column(u'clientes_cliente', 'facturacion_calle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Cliente.facturacion_numero'
        db.add_column(u'clientes_cliente', 'facturacion_numero',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Cliente.facturacion_cp'
        db.add_column(u'clientes_cliente', 'facturacion_cp',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.recoleccion_clave_municipio'
        db.add_column(u'clientes_cliente', 'recoleccion_clave_municipio',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Cliente.recoleccion_colonia'
        db.add_column(u'clientes_cliente', 'recoleccion_colonia',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Cliente.recoleccion_calle'
        db.add_column(u'clientes_cliente', 'recoleccion_calle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Cliente.recoleccion_numero'
        db.add_column(u'clientes_cliente', 'recoleccion_numero',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Cliente.recoleccion_cp'
        db.add_column(u'clientes_cliente', 'recoleccion_cp',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ClienteAuditLogEntry.numero'
        raise RuntimeError("Cannot reverse this migration. 'ClienteAuditLogEntry.numero' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ClienteAuditLogEntry.numero'
        db.add_column(u'clientes_clienteauditlogentry', 'numero',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ClienteAuditLogEntry.estado'
        raise RuntimeError("Cannot reverse this migration. 'ClienteAuditLogEntry.estado' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ClienteAuditLogEntry.estado'
        db.add_column(u'clientes_clienteauditlogentry', 'estado',
                      self.gf('django.db.models.fields.CharField')(max_length=3),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ClienteAuditLogEntry.municipio'
        raise RuntimeError("Cannot reverse this migration. 'ClienteAuditLogEntry.municipio' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ClienteAuditLogEntry.municipio'
        db.add_column(u'clientes_clienteauditlogentry', 'municipio',
                      self.gf('django.db.models.fields.CharField')(max_length=150),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ClienteAuditLogEntry.colonia'
        raise RuntimeError("Cannot reverse this migration. 'ClienteAuditLogEntry.colonia' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ClienteAuditLogEntry.colonia'
        db.add_column(u'clientes_clienteauditlogentry', 'colonia',
                      self.gf('django.db.models.fields.CharField')(max_length=150),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ClienteAuditLogEntry.calle'
        raise RuntimeError("Cannot reverse this migration. 'ClienteAuditLogEntry.calle' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ClienteAuditLogEntry.calle'
        db.add_column(u'clientes_clienteauditlogentry', 'calle',
                      self.gf('django.db.models.fields.CharField')(max_length=150),
                      keep_default=False)

        # Deleting field 'ClienteAuditLogEntry.facturacion_clave_municipio'
        db.delete_column(u'clientes_clienteauditlogentry', 'facturacion_clave_municipio')

        # Deleting field 'ClienteAuditLogEntry.facturacion_colonia'
        db.delete_column(u'clientes_clienteauditlogentry', 'facturacion_colonia')

        # Deleting field 'ClienteAuditLogEntry.facturacion_calle'
        db.delete_column(u'clientes_clienteauditlogentry', 'facturacion_calle')

        # Deleting field 'ClienteAuditLogEntry.facturacion_numero'
        db.delete_column(u'clientes_clienteauditlogentry', 'facturacion_numero')

        # Deleting field 'ClienteAuditLogEntry.facturacion_cp'
        db.delete_column(u'clientes_clienteauditlogentry', 'facturacion_cp')

        # Deleting field 'ClienteAuditLogEntry.recoleccion_clave_municipio'
        db.delete_column(u'clientes_clienteauditlogentry', 'recoleccion_clave_municipio')

        # Deleting field 'ClienteAuditLogEntry.recoleccion_colonia'
        db.delete_column(u'clientes_clienteauditlogentry', 'recoleccion_colonia')

        # Deleting field 'ClienteAuditLogEntry.recoleccion_calle'
        db.delete_column(u'clientes_clienteauditlogentry', 'recoleccion_calle')

        # Deleting field 'ClienteAuditLogEntry.recoleccion_numero'
        db.delete_column(u'clientes_clienteauditlogentry', 'recoleccion_numero')

        # Deleting field 'ClienteAuditLogEntry.recoleccion_cp'
        db.delete_column(u'clientes_clienteauditlogentry', 'recoleccion_cp')


        # User chose to not deal with backwards NULL issues for 'Cliente.calle'
        raise RuntimeError("Cannot reverse this migration. 'Cliente.calle' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Cliente.calle'
        db.add_column(u'clientes_cliente', 'calle',
                      self.gf('django.db.models.fields.CharField')(max_length=150),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Cliente.numero'
        raise RuntimeError("Cannot reverse this migration. 'Cliente.numero' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Cliente.numero'
        db.add_column(u'clientes_cliente', 'numero',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Cliente.colonia'
        raise RuntimeError("Cannot reverse this migration. 'Cliente.colonia' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Cliente.colonia'
        db.add_column(u'clientes_cliente', 'colonia',
                      self.gf('django.db.models.fields.CharField')(max_length=150),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Cliente.estado'
        raise RuntimeError("Cannot reverse this migration. 'Cliente.estado' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Cliente.estado'
        db.add_column(u'clientes_cliente', 'estado',
                      self.gf('django.db.models.fields.CharField')(max_length=3),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Cliente.municipio'
        raise RuntimeError("Cannot reverse this migration. 'Cliente.municipio' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Cliente.municipio'
        db.add_column(u'clientes_cliente', 'municipio',
                      self.gf('django.db.models.fields.CharField')(max_length=150),
                      keep_default=False)

        # Deleting field 'Cliente.facturacion_clave_municipio'
        db.delete_column(u'clientes_cliente', 'facturacion_clave_municipio')

        # Deleting field 'Cliente.facturacion_colonia'
        db.delete_column(u'clientes_cliente', 'facturacion_colonia')

        # Deleting field 'Cliente.facturacion_calle'
        db.delete_column(u'clientes_cliente', 'facturacion_calle')

        # Deleting field 'Cliente.facturacion_numero'
        db.delete_column(u'clientes_cliente', 'facturacion_numero')

        # Deleting field 'Cliente.facturacion_cp'
        db.delete_column(u'clientes_cliente', 'facturacion_cp')

        # Deleting field 'Cliente.recoleccion_clave_municipio'
        db.delete_column(u'clientes_cliente', 'recoleccion_clave_municipio')

        # Deleting field 'Cliente.recoleccion_colonia'
        db.delete_column(u'clientes_cliente', 'recoleccion_colonia')

        # Deleting field 'Cliente.recoleccion_calle'
        db.delete_column(u'clientes_cliente', 'recoleccion_calle')

        # Deleting field 'Cliente.recoleccion_numero'
        db.delete_column(u'clientes_cliente', 'recoleccion_numero')

        # Deleting field 'Cliente.recoleccion_cp'
        db.delete_column(u'clientes_cliente', 'recoleccion_cp')


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
            'recoleccion_numero': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'clientes.clienteauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'ClienteAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_cliente_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'facturacion_calle': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'facturacion_clave_municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'facturacion_colonia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'facturacion_cp': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'facturacion_numero': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'recoleccion_calle': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'recoleccion_clave_municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recoleccion_colonia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'recoleccion_cp': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'recoleccion_numero': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'clientes.departamento': {
            'Meta': {'ordering': "['departamento']", 'object_name': 'Departamento'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'departamento': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'clientes.departamentoauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'DepartamentoAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_departamento_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'departamento': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['clientes']