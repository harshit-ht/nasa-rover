# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'minerals'
        db.delete_table(u'rover_minerals')

        # Adding model 'mineral'
        db.create_table(u'rover_mineral', (
            ('mineral_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mineral_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'rover', ['mineral'])


    def backwards(self, orm):
        # Adding model 'minerals'
        db.create_table(u'rover_minerals', (
            ('mineral_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mineral_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'rover', ['minerals'])

        # Deleting model 'mineral'
        db.delete_table(u'rover_mineral')


    models = {
        u'rover.grid': {
            'Meta': {'object_name': 'Grid'},
            'grid_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'grid_sizex': ('django.db.models.fields.IntegerField', [], {}),
            'grid_sizey': ('django.db.models.fields.IntegerField', [], {})
        },
        u'rover.mineral': {
            'Meta': {'object_name': 'mineral'},
            'mineral_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mineral_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'rover.mineral_distribution': {
            'Meta': {'object_name': 'Mineral_Distribution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mineral_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mineral_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'subgrid_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rover.Subgrid']"})
        },
        u'rover.rover': {
            'Meta': {'object_name': 'Rover'},
            'rover_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rover_initdirection': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'rover_initposx': ('django.db.models.fields.IntegerField', [], {}),
            'rover_initposy': ('django.db.models.fields.IntegerField', [], {}),
            'rover_movement': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rover_sense': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rover.mineral']", 'symmetrical': 'False'}),
            'rovergrid_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rover.Grid']"})
        },
        u'rover.roverdetails': {
            'Meta': {'object_name': 'Roverdetails'},
            'rover_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'roverdetail_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'rover.subgrid': {
            'Meta': {'object_name': 'Subgrid'},
            'grid_ids': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rover.Grid']"}),
            'subgrid_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subgrid_posx': ('django.db.models.fields.IntegerField', [], {}),
            'subgrid_posy': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['rover']