from django.contrib import admin
from rover.models import Grid, Subgrid, mineral, Rover, Mineral_Distribution, Roverdetails

class SubgridAdmin(admin.ModelAdmin):
    list_display = ('subgrid_id','subgrid_posx','subgrid_posy','grid_ids')
    search_fields = ('subgrid_posx',)

class MineraldistAdmin(admin.ModelAdmin):
    list_display = ('mineral_name','mineral_quantity','subgrid_id','id')
    
admin.site.register(Roverdetails)
admin.site.register(Grid)
admin.site.register(Subgrid,SubgridAdmin)
admin.site.register(mineral)
admin.site.register(Rover)
admin.site.register(Mineral_Distribution, MineraldistAdmin)
# Register your models here.

