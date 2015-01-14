# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'mineral'
        db.create_table(u'rover_mineral', (
            ('mineral_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mineral_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'rover', ['mineral'])

        # Adding model 'Grid'
        db.create_table(u'rover_grid', (
            ('grid_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grid_sizex', self.gf('django.db.models.fields.IntegerField')()),
            ('grid_sizey', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'rover', ['Grid'])

        # Adding model 'Subgrid'
        db.create_table(u'rover_subgrid', (
            ('subgrid_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subgrid_posx', self.gf('django.db.models.fields.IntegerField')()),
            ('subgrid_posy', self.gf('django.db.models.fields.IntegerField')()),
            ('grid_ids', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rover.Grid'])),
        ))
        db.send_create_signal(u'rover', ['Subgrid'])

        # Adding model 'Mineral_Distribution'
        db.create_table(u'rover_mineral_distribution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mineral_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mineral_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('subgrid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rover.Subgrid'])),
        ))
        db.send_create_signal(u'rover', ['Mineral_Distribution'])

        # Adding model 'Roverdetails'
        db.create_table(u'rover_roverdetails', (
            ('roverdetail_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rover_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'rover', ['Roverdetails'])

        # Adding model 'Rover'
        db.create_table(u'rover_rover', (
            ('rover_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rover_initposx', self.gf('django.db.models.fields.IntegerField')()),
            ('rover_initposy', self.gf('django.db.models.fields.IntegerField')()),
            ('rover_initdirection', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('rover_movement', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rovergrid_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rover.Grid'])),
        ))
        db.send_create_signal(u'rover', ['Rover'])

        # Adding M2M table for field rover_sense on 'Rover'
        m2m_table_name = db.shorten_name(u'rover_rover_rover_sense')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('rover', models.ForeignKey(orm[u'rover.rover'], null=False)),
            ('mineral', models.ForeignKey(orm[u'rover.mineral'], null=False))
        ))
        db.create_unique(m2m_table_name, ['rover_id', 'mineral_id'])


    def backwards(self, orm):
        # Deleting model 'mineral'
        db.delete_table(u'rover_mineral')

        # Deleting model 'Grid'
        db.delete_table(u'rover_grid')

        # Deleting model 'Subgrid'
        db.delete_table(u'rover_subgrid')

        # Deleting model 'Mineral_Distribution'
        db.delete_table(u'rover_mineral_distribution')

        # Deleting model 'Roverdetails'
        db.delete_table(u'rover_roverdetails')

        # Deleting model 'Rover'
        db.delete_table(u'rover_rover')

        # Removing M2M table for field rover_sense on 'Rover'
        db.delete_table(db.shorten_name(u'rover_rover_rover_sense'))


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