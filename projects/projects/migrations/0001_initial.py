# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'projects_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total_pledged', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'projects', ['Category'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pledged', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'projects', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'projects_category')

        # Deleting model 'Project'
        db.delete_table(u'projects_project')


    models = {
        u'projects.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'total_pledged': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pledged': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['projects']