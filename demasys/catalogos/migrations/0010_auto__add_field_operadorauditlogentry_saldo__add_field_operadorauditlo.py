# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'OperadorAuditLogEntry.saldo'
        db.add_column(u'catalogos_operadorauditlogentry', 'saldo',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2),
                      keep_default=False)

        # Adding field 'OperadorAuditLogEntry.saldo_observaciones'
        db.add_column(u'catalogos_operadorauditlogentry', 'saldo_observaciones',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Operador.saldo'
        db.add_column(u'catalogos_operador', 'saldo',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2),
                      keep_default=False)

        # Adding field 'Operador.saldo_observaciones'
        db.add_column(u'catalogos_operador', 'saldo_observaciones',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Economico.saldo'
        db.add_column(u'catalogos_economico', 'saldo',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2),
                      keep_default=False)

        # Adding field 'Economico.saldo_observaciones'
        db.add_column(u'catalogos_economico', 'saldo_observaciones',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'EconomicoAuditLogEntry.saldo'
        db.add_column(u'catalogos_economicoauditlogentry', 'saldo',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2),
                      keep_default=False)

        # Adding field 'EconomicoAuditLogEntry.saldo_observaciones'
        db.add_column(u'catalogos_economicoauditlogentry', 'saldo_observaciones',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'OperadorAuditLogEntry.saldo'
        db.delete_column(u'catalogos_operadorauditlogentry', 'saldo')

        # Deleting field 'OperadorAuditLogEntry.saldo_observaciones'
        db.delete_column(u'catalogos_operadorauditlogentry', 'saldo_observaciones')

        # Deleting field 'Operador.saldo'
        db.delete_column(u'catalogos_operador', 'saldo')

        # Deleting field 'Operador.saldo_observaciones'
        db.delete_column(u'catalogos_operador', 'saldo_observaciones')

        # Deleting field 'Economico.saldo'
        db.delete_column(u'catalogos_economico', 'saldo')

        # Deleting field 'Economico.saldo_observaciones'
        db.delete_column(u'catalogos_economico', 'saldo_observaciones')

        # Deleting field 'EconomicoAuditLogEntry.saldo'
        db.delete_column(u'catalogos_economicoauditlogentry', 'saldo')

        # Deleting field 'EconomicoAuditLogEntry.saldo_observaciones'
        db.delete_column(u'catalogos_economicoauditlogentry', 'saldo_observaciones')


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
        u'catalogos.casetaauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'CasetaAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_caseta_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'autobus_2_ejes': ('django.db.models.fields.FloatField', [], {}),
            'autos': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'via': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'catalogos.conceptofacturacion': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'ConceptoFacturacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'catalogos.conceptofacturacionauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'ConceptoFacturacionAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_conceptofacturacion_audit_log_entry'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'catalogos.economico': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Economico'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogos.ModeloEconomico']"}),
            'pasa_como': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'placas': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'saldo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'saldo_observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'catalogos.economicoauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'EconomicoAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_economico_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'modelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogos.ModeloEconomico']"}),
            'pasa_como': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'placas': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'saldo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'saldo_observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'catalogos.gastoviaje': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'GastoViaje'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'catalogos.gastoviajeauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'GastoViajeAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_gastoviaje_audit_log_entry'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'catalogos.modeloeconomico': {
            'Meta': {'ordering': "['modelo']", 'object_name': 'ModeloEconomico'},
            'capacidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'catalogos.modeloeconomicoauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'ModeloEconomicoAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_modeloeconomico_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'capacidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'catalogos.operador': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Operador'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'saldo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'saldo_observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'catalogos.operadorauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'OperadorAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_operador_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'saldo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'saldo_observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['catalogos']