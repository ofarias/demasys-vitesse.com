# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Sepomex'
        db.create_table('sepomex_sepomex', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('asentamiento', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tipo_asentamiento', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('clave_estado', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('clave_oficina', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('clave_tipo_asenta', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('clave_municipio', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id_asenta_cpcons', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('d_zona', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c_cve_ciudad', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c_CP', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('sepomex', ['Sepomex'])


    def backwards(self, orm):
        
        # Deleting model 'Sepomex'
        db.delete_table('sepomex_sepomex')


    models = {
        'sepomex.sepomex': {
            'Meta': {'object_name': 'Sepomex'},
            'asentamiento': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c_CP': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c_cve_ciudad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'clave_estado': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'clave_municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'clave_oficina': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'clave_tipo_asenta': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'd_zona': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_asenta_cpcons': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tipo_asentamiento': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sepomex']
