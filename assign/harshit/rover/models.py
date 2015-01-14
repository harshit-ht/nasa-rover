from django.db import models
from random import randint
from django.db.models.signals import post_save, pre_save, pre_init, post_init
class mineral(models.Model):
    mineral_id = models.AutoField(primary_key = True)
    mineral_name = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.mineral_name

class Grid(models.Model):
    grid_id = models.AutoField(primary_key = True)
    grid_sizex = models.IntegerField()
    grid_sizey = models.IntegerField()
    
    
class Subgrid(models.Model):
    subgrid_id = models.AutoField(primary_key = True)
    subgrid_posx = models.IntegerField()
    subgrid_posy = models.IntegerField()
    grid_ids = models.ForeignKey(Grid)
    
class Mineral_Distribution(models.Model):
    mineral_name  = models.CharField(max_length = 100)
    mineral_quantity = models.IntegerField()
    subgrid_id = models.ForeignKey(Subgrid)

class Roverdetails(models.Model):
    roverdetail_id = models.AutoField(primary_key = True)
    rover_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.rover_name

class Rover(models.Model):
    rover_id = models.AutoField(primary_key = True)
    rover_detail = models.ForeignKey(Roverdetails)
    rover_initposx = models.IntegerField()
    rover_initposy = models.IntegerField()
    rover_initdirection = models.CharField(max_length = 1)
    rover_movement = models.CharField(max_length = 100)
    rover_sense = models.ManyToManyField(mineral)
    rovergrid_id = models.ForeignKey(Grid)

def addminerals(sender,instance,**kwargs):
    for i in range(instance.grid_sizex):
        for j in range(instance.grid_sizey):
            p = Subgrid(subgrid_posx=i, subgrid_posy=j, grid_ids = instance)
            p.save()
            for k in mineral.objects.all():
                Mineral_Distribution.objects.create(mineral_name = k.mineral_name, mineral_quantity = randint(0,4),subgrid_id = p)

post_save.connect(addminerals, sender = Grid)