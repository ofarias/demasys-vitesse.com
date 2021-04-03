# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ModeloEconomicoAuditLogEntry'
        db.create_table(u'catalogos_modeloeconomicoauditlogentry', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('capacidad', self.gf('django.db.models.fields.IntegerField')()),
            ('action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('action_user', self.gf('audit_log.models.fields.LastUserField')(related_name='_modeloeconomico_audit_log_entry', to=orm['auth.User'])),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'catalogos', ['ModeloEconomicoAuditLogEntry'])

        # Adding model 'ModeloEconomico'
        db.create_table(u'catalogos_modeloeconomico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('capacidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'catalogos', ['ModeloEconomico'])

        # Adding model 'EconomicoAuditLogEntry'
        db.create_table(u'catalogos_economicoauditlogentry', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('modelo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogos.ModeloEconomico'])),
            ('placas', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('action_user', self.gf('audit_log.models.fields.LastUserField')(related_name='_economico_audit_log_entry', to=orm['auth.User'])),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'catalogos', ['EconomicoAuditLogEntry'])

        # Adding model 'Economico'
        db.create_table(u'catalogos_economico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('modelo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogos.ModeloEconomico'])),
            ('placas', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'catalogos', ['Economico'])

        # Adding model 'OperadorAuditLogEntry'
        db.create_table(u'catalogos_operadorauditlogentry', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellido_paterno', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('apellido_materno', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('action_user', self.gf('audit_log.models.fields.LastUserField')(related_name='_operador_audit_log_entry', to=orm['auth.User'])),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'catalogos', ['OperadorAuditLogEntry'])

        # Adding model 'Operador'
        db.create_table(u'catalogos_operador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellido_paterno', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('apellido_materno', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'catalogos', ['Operador'])


    def backwards(self, orm):
        # Deleting model 'ModeloEconomicoAuditLogEntry'
        db.delete_table(u'catalogos_modeloeconomicoauditlogentry')

        # Deleting model 'ModeloEconomico'
        db.delete_table(u'catalogos_modeloeconomico')

        # Deleting model 'EconomicoAuditLogEntry'
        db.delete_table(u'catalogos_economicoauditlogentry')

        # Deleting model 'Economico'
        db.delete_table(u'catalogos_economico')

        # Deleting model 'OperadorAuditLogEntry'
        db.delete_table(u'catalogos_operadorauditlogentry')

        # Deleting model 'Operador'
        db.delete_table(u'catalogos_operador')


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
        u'catalogos.economico': {
            'Meta': {'object_name': 'Economico'},
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
            'Meta': {'object_name': 'ModeloEconomico'},
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
            'Meta': {'object_name': 'Operador'},
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'catalogos.operadorauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'OperadorAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_operador_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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