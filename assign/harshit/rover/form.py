from django.forms import ModelForm
from rover.models import Rover, Grid

class Roverform(ModelForm):
    class Meta:
        model = Rover
        
class Gridform(ModelForm):
    class Meta:
        model = Grid
        fields = ['grid_sizex','grid_sizey']
