# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CasetaAuditLogEntry.camion_9_ejes'
        db.delete_column(u'catalogos_casetaauditlogentry', 'camion_9_ejes')

        # Deleting field 'CasetaAuditLogEntry.longitud'
        db.delete_column(u'catalogos_casetaauditlogentry', 'longitud')

        # Deleting field 'CasetaAuditLogEntry.autobus_4_ejes'
        db.delete_column(u'catalogos_casetaauditlogentry', 'autobus_4_ejes')

        # Deleting field 'CasetaAuditLogEntry.camion_6_ejes'
        db.delete_column(u'catalogos_casetaauditlogentry', 'camion_6_ejes')

        # Deleting field 'CasetaAuditLogEntry.camion_5_ejes'
        db.delete_column(u'catalogos_casetaauditlogentry', 'camion_5_ejes')

        # Deleting field 'CasetaAuditLogEntry.camion_7_ejes'
        db.delete_column(u'catalogos_casetaauditlogentry', 'camion_7_ejes')

        # Deleting field 'CasetaAuditLogEntry.camion_2_ejes'
        db.delete_column(u'catalogos_casetaauditlogentry', 'camion_2_ejes')

        # Deleting field 'CasetaAuditLogEntry.motos'
        db.delete_column(u'catalogos_casetaauditlogentry', 'motos')

        # Deleting field 'CasetaAuditLogEntry.camion_8_ejes'
        db.delete_column(u'catalogos_casetaauditlogentry', 'camion_8_ejes')

        # Deleting field 'CasetaAuditLogEntry.camion_4_ejes'
        db.delete_column(u'catalogos_casetaauditlogentry', 'camion_4_ejes')

        # Deleting field 'CasetaAuditLogEntry.autobus_3_ejes'
        db.delete_column(u'catalogos_casetaauditlogentry', 'autobus_3_ejes')

        # Deleting field 'CasetaAuditLogEntry.camion_3_ejes'
        db.delete_column(u'catalogos_casetaauditlogentry', 'camion_3_ejes')

        # Deleting field 'Caseta.camion_9_ejes'
        db.delete_column(u'catalogos_caseta', 'camion_9_ejes')

        # Deleting field 'Caseta.longitud'
        db.delete_column(u'catalogos_caseta', 'longitud')

        # Deleting field 'Caseta.autobus_4_ejes'
        db.delete_column(u'catalogos_caseta', 'autobus_4_ejes')

        # Deleting field 'Caseta.camion_6_ejes'
        db.delete_column(u'catalogos_caseta', 'camion_6_ejes')

        # Deleting field 'Caseta.camion_5_ejes'
        db.delete_column(u'catalogos_caseta', 'camion_5_ejes')

        # Deleting field 'Caseta.camion_7_ejes'
        db.delete_column(u'catalogos_caseta', 'camion_7_ejes')

        # Deleting field 'Caseta.camion_4_ejes'
        db.delete_column(u'catalogos_caseta', 'camion_4_ejes')

        # Deleting field 'Caseta.camion_2_ejes'
        db.delete_column(u'catalogos_caseta', 'camion_2_ejes')

        # Deleting field 'Caseta.motos'
        db.delete_column(u'catalogos_caseta', 'motos')

        # Deleting field 'Caseta.camion_8_ejes'
        db.delete_column(u'catalogos_caseta', 'camion_8_ejes')

        # Deleting field 'Caseta.autobus_3_ejes'
        db.delete_column(u'catalogos_caseta', 'autobus_3_ejes')

        # Deleting field 'Caseta.camion_3_ejes'
        db.delete_column(u'catalogos_caseta', 'camion_3_ejes')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.camion_9_ejes'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.camion_9_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.camion_9_ejes'
        db.add_column(u'catalogos_casetaauditlogentry', 'camion_9_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.longitud'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.longitud' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.longitud'
        db.add_column(u'catalogos_casetaauditlogentry', 'longitud',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.autobus_4_ejes'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.autobus_4_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.autobus_4_ejes'
        db.add_column(u'catalogos_casetaauditlogentry', 'autobus_4_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.camion_6_ejes'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.camion_6_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.camion_6_ejes'
        db.add_column(u'catalogos_casetaauditlogentry', 'camion_6_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.camion_5_ejes'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.camion_5_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.camion_5_ejes'
        db.add_column(u'catalogos_casetaauditlogentry', 'camion_5_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.camion_7_ejes'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.camion_7_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.camion_7_ejes'
        db.add_column(u'catalogos_casetaauditlogentry', 'camion_7_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.camion_2_ejes'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.camion_2_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.camion_2_ejes'
        db.add_column(u'catalogos_casetaauditlogentry', 'camion_2_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.motos'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.motos' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.motos'
        db.add_column(u'catalogos_casetaauditlogentry', 'motos',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.camion_8_ejes'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.camion_8_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.camion_8_ejes'
        db.add_column(u'catalogos_casetaauditlogentry', 'camion_8_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.camion_4_ejes'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.camion_4_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.camion_4_ejes'
        db.add_column(u'catalogos_casetaauditlogentry', 'camion_4_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.autobus_3_ejes'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.autobus_3_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.autobus_3_ejes'
        db.add_column(u'catalogos_casetaauditlogentry', 'autobus_3_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CasetaAuditLogEntry.camion_3_ejes'
        raise RuntimeError("Cannot reverse this migration. 'CasetaAuditLogEntry.camion_3_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CasetaAuditLogEntry.camion_3_ejes'
        db.add_column(u'catalogos_casetaauditlogentry', 'camion_3_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.camion_9_ejes'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.camion_9_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.camion_9_ejes'
        db.add_column(u'catalogos_caseta', 'camion_9_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.longitud'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.longitud' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.longitud'
        db.add_column(u'catalogos_caseta', 'longitud',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.autobus_4_ejes'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.autobus_4_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.autobus_4_ejes'
        db.add_column(u'catalogos_caseta', 'autobus_4_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.camion_6_ejes'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.camion_6_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.camion_6_ejes'
        db.add_column(u'catalogos_caseta', 'camion_6_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.camion_5_ejes'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.camion_5_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.camion_5_ejes'
        db.add_column(u'catalogos_caseta', 'camion_5_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.camion_7_ejes'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.camion_7_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.camion_7_ejes'
        db.add_column(u'catalogos_caseta', 'camion_7_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.camion_4_ejes'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.camion_4_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.camion_4_ejes'
        db.add_column(u'catalogos_caseta', 'camion_4_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.camion_2_ejes'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.camion_2_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.camion_2_ejes'
        db.add_column(u'catalogos_caseta', 'camion_2_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.motos'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.motos' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.motos'
        db.add_column(u'catalogos_caseta', 'motos',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.camion_8_ejes'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.camion_8_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.camion_8_ejes'
        db.add_column(u'catalogos_caseta', 'camion_8_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.autobus_3_ejes'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.autobus_3_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.autobus_3_ejes'
        db.add_column(u'catalogos_caseta', 'autobus_3_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Caseta.camion_3_ejes'
        raise RuntimeError("Cannot reverse this migration. 'Caseta.camion_3_ejes' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Caseta.camion_3_ejes'
        db.add_column(u'catalogos_caseta', 'camion_3_ejes',
                      self.gf('django.db.models.fields.FloatField')(),
                      keep_default=False)


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
        u'catalogos.economico': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Economico'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogos.ModeloEconomico']"}),
            'placas': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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
            'placas': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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