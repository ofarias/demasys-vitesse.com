# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Role'
        db.create_table(u'workflow_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'workflow', ['Role'])

        # Adding model 'Workflow'
        db.create_table(u'workflow_workflow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('cloned_from', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflow.Workflow'], null=True)),
        ))
        db.send_create_signal(u'workflow', ['Workflow'])

        # Adding model 'State'
        db.create_table(u'workflow_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_start_state', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_end_state', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('workflow', self.gf('django.db.models.fields.related.ForeignKey')(related_name='states', to=orm['workflow.Workflow'])),
            ('estimation_value', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('estimation_unit', self.gf('django.db.models.fields.IntegerField')(default=86400)),
        ))
        db.send_create_signal(u'workflow', ['State'])

        # Adding M2M table for field roles on 'State'
        m2m_table_name = db.shorten_name(u'workflow_state_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('state', models.ForeignKey(orm[u'workflow.state'], null=False)),
            ('role', models.ForeignKey(orm[u'workflow.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['state_id', 'role_id'])

        # Adding model 'Transition'
        db.create_table(u'workflow_transition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('workflow', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transitions', to=orm['workflow.Workflow'])),
            ('from_state', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transitions_from', to=orm['workflow.State'])),
            ('to_state', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transitions_into', to=orm['workflow.State'])),
        ))
        db.send_create_signal(u'workflow', ['Transition'])

        # Adding M2M table for field roles on 'Transition'
        m2m_table_name = db.shorten_name(u'workflow_transition_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('transition', models.ForeignKey(orm[u'workflow.transition'], null=False)),
            ('role', models.ForeignKey(orm[u'workflow.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['transition_id', 'role_id'])

        # Adding model 'EventType'
        db.create_table(u'workflow_eventtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'workflow', ['EventType'])

        # Adding model 'Event'
        db.create_table(u'workflow_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('workflow', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='events', null=True, to=orm['workflow.Workflow'])),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='events', null=True, to=orm['workflow.State'])),
            ('is_mandatory', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'workflow', ['Event'])

        # Adding M2M table for field roles on 'Event'
        m2m_table_name = db.shorten_name(u'workflow_event_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'workflow.event'], null=False)),
            ('role', models.ForeignKey(orm[u'workflow.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'role_id'])

        # Adding M2M table for field event_types on 'Event'
        m2m_table_name = db.shorten_name(u'workflow_event_event_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'workflow.event'], null=False)),
            ('eventtype', models.ForeignKey(orm[u'workflow.eventtype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'eventtype_id'])

        # Adding model 'WorkflowActivity'
        db.create_table(u'workflow_workflowactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workflow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflow.Workflow'])),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('completed_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'workflow', ['WorkflowActivity'])

        # Adding model 'Participant'
        db.create_table(u'workflow_participant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('workflowactivity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='participants', to=orm['workflow.WorkflowActivity'])),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'workflow', ['Participant'])

        # Adding unique constraint on 'Participant', fields ['user', 'workflowactivity']
        db.create_unique(u'workflow_participant', ['user_id', 'workflowactivity_id'])

        # Adding M2M table for field roles on 'Participant'
        m2m_table_name = db.shorten_name(u'workflow_participant_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participant', models.ForeignKey(orm[u'workflow.participant'], null=False)),
            ('role', models.ForeignKey(orm[u'workflow.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['participant_id', 'role_id'])

        # Adding model 'WorkflowHistory'
        db.create_table(u'workflow_workflowhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workflowactivity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='history', to=orm['workflow.WorkflowActivity'])),
            ('log_type', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflow.State'], null=True)),
            ('transition', self.gf('django.db.models.fields.related.ForeignKey')(related_name='history', null=True, to=orm['workflow.Transition'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='history', null=True, to=orm['workflow.Event'])),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflow.Participant'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('deadline', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'workflow', ['WorkflowHistory'])


    def backwards(self, orm):
        # Removing unique constraint on 'Participant', fields ['user', 'workflowactivity']
        db.delete_unique(u'workflow_participant', ['user_id', 'workflowactivity_id'])

        # Deleting model 'Role'
        db.delete_table(u'workflow_role')

        # Deleting model 'Workflow'
        db.delete_table(u'workflow_workflow')

        # Deleting model 'State'
        db.delete_table(u'workflow_state')

        # Removing M2M table for field roles on 'State'
        db.delete_table(db.shorten_name(u'workflow_state_roles'))

        # Deleting model 'Transition'
        db.delete_table(u'workflow_transition')

        # Removing M2M table for field roles on 'Transition'
        db.delete_table(db.shorten_name(u'workflow_transition_roles'))

        # Deleting model 'EventType'
        db.delete_table(u'workflow_eventtype')

        # Deleting model 'Event'
        db.delete_table(u'workflow_event')

        # Removing M2M table for field roles on 'Event'
        db.delete_table(db.shorten_name(u'workflow_event_roles'))

        # Removing M2M table for field event_types on 'Event'
        db.delete_table(db.shorten_name(u'workflow_event_event_types'))

        # Deleting model 'WorkflowActivity'
        db.delete_table(u'workflow_workflowactivity')

        # Deleting model 'Participant'
        db.delete_table(u'workflow_participant')

        # Removing M2M table for field roles on 'Participant'
        db.delete_table(db.shorten_name(u'workflow_participant_roles'))

        # Deleting model 'WorkflowHistory'
        db.delete_table(u'workflow_workflowhistory')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'workflow.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['workflow.EventType']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_mandatory': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['workflow.Role']", 'symmetrical': 'False'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'events'", 'null': 'True', 'to': u"orm['workflow.State']"}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'events'", 'null': 'True', 'to': u"orm['workflow.Workflow']"})
        },
        u'workflow.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'workflow.participant': {
            'Meta': {'ordering': "['-disabled', 'workflowactivity', 'user']", 'unique_together': "(('user', 'workflowactivity'),)", 'object_name': 'Participant'},
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['workflow.Role']", 'null': 'True', 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'workflowactivity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participants'", 'to': u"orm['workflow.WorkflowActivity']"})
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
        u'workflow.transition': {
            'Meta': {'object_name': 'Transition'},
            'from_state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transitions_from'", 'to': u"orm['workflow.State']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['workflow.Role']", 'symmetrical': 'False', 'blank': 'True'}),
            'to_state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transitions_into'", 'to': u"orm['workflow.State']"}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transitions'", 'to': u"orm['workflow.Workflow']"})
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
        },
        u'workflow.workflowhistory': {
            'Meta': {'ordering': "['-created_on']", 'object_name': 'WorkflowHistory'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history'", 'null': 'True', 'to': u"orm['workflow.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_type': ('django.db.models.fields.IntegerField', [], {}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workflow.Participant']"}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workflow.State']", 'null': 'True'}),
            'transition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history'", 'null': 'True', 'to': u"orm['workflow.Transition']"}),
            'workflowactivity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history'", 'to': u"orm['workflow.WorkflowActivity']"})
        }
    }

    complete_apps = ['workflow']