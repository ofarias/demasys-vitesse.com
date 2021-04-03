# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClienteAuditLogEntry'
        db.create_table(u'clientes_clienteauditlogentry', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('calle', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('action_user', self.gf('audit_log.models.fields.LastUserField')(related_name='_cliente_audit_log_entry', to=orm['auth.User'])),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'clientes', ['ClienteAuditLogEntry'])

        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('calle', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])


    def backwards(self, orm):
        # Deleting model 'ClienteAuditLogEntry'
        db.delete_table(u'clientes_clienteauditlogentry')

        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')


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
            'Meta': {'ordering': "['nombre']", 'object_name': 'Cliente'},
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'clientes.clienteauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'ClienteAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_cliente_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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