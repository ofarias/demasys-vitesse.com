# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Sepomex.asentamiento'
        db.alter_column('sepomex_sepomex', 'asentamiento', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Sepomex.estado'
        db.alter_column('sepomex_sepomex', 'estado', self.gf('django.db.models.fields.CharField')(max_length=120))

        # Changing field 'Sepomex.ciudad'
        db.alter_column('sepomex_sepomex', 'ciudad', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Sepomex.tipo_asentamiento'
        db.alter_column('sepomex_sepomex', 'tipo_asentamiento', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Sepomex.municipio'
        db.alter_column('sepomex_sepomex', 'municipio', self.gf('django.db.models.fields.CharField')(max_length=255))


    def backwards(self, orm):
        
        # Changing field 'Sepomex.asentamiento'
        db.alter_column('sepomex_sepomex', 'asentamiento', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Sepomex.estado'
        db.alter_column('sepomex_sepomex', 'estado', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Sepomex.ciudad'
        db.alter_column('sepomex_sepomex', 'ciudad', self.gf('django.db.models.fields.CharField')(max_length=45))

        # Changing field 'Sepomex.tipo_asentamiento'
        db.alter_column('sepomex_sepomex', 'tipo_asentamiento', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Sepomex.municipio'
        db.alter_column('sepomex_sepomex', 'municipio', self.gf('django.db.models.fields.CharField')(max_length=100))


    models = {
        'sepomex.sepomex': {
            'Meta': {'object_name': 'Sepomex'},
            'asentamiento': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'c_CP': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c_cve_ciudad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'clave_estado': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'clave_municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'clave_oficina': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'clave_tipo_asenta': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'd_zona': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_asenta_cpcons': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo_asentamiento': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['sepomex']
