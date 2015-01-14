from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import RequestContext
from rover.models import Rover, Grid, addminerals, Mineral_Distribution, Subgrid 
from rover.form import Roverform, Gridform

def creating_grid(request):
    if request.method == "POST":
        gridform = Gridform(request.POST)
        if gridform.is_valid():
            cd = gridform.cleaned_data
            k = Grid.objects.create(grid_sizex = cd['grid_sizex'],grid_sizey = cd['grid_sizey'])
            
            return HttpResponseRedirect("/")
        else:
            return render_to_response("creategrid.html",{"gridform":gridform}, context_instance = RequestContext(request))         
    else:
        gridform = Gridform()
        return render_to_response("creategrid.html",{"gridform":gridform}, context_instance = RequestContext(request))
        
def roverworking(posx, posy, direct, movement, sense, rovergrid):
    l = []
    for i in range(len(movement)):
        if movement[i] == 'M':
            if direct == 'N':
                posx = posx + 1
                x = consumption(posx, posy, sense, rovergrid)
                l.append(x)
            elif direct == 'S':
                posx = posx - 1
                x = consumption(posx, posy, sense, rovergrid)
                l.append(x)
            elif direct == 'E':
                posy = posy + 1
                x = consumption(posx, posy, sense, rovergrid)
                l.append(x)
            elif direct == 'W':
                posy = posy - 1
                x = consumption(posx, posy, sense, rovergrid)
                l.append(x)
        elif movement[i] == 'L':
            if direct == 'W':
                direct = 'S'
            elif direct == 'E':
                direct = 'N'
            elif direct == 'N':
                direct = 'W'
            elif direct == 'S':
                direct = 'E'
        elif movement[i] == 'R':
            if direct == 'W':
                direct = 'N'
            elif direct == 'E':
                direct = 'S'
            elif direct == 'N':
                direct = 'E'
            elif direct == 'S':
                direct = 'W'
                
    return HttpResponse(("FINAL DIRECTION=",direct,"   ","FINAL X POSITION IS:",posx,"   ","FINAL Y POSITION IS :",posy,"   ",l))
                
def consumption(posx, posy, senses, rovergrid):
    temp = []
    
    print temp
    s = Subgrid.objects.filter(subgrid_posx = posx, subgrid_posy = posy, grid_ids = rovergrid)
    for mineral in senses:
        print mineral
        l = Mineral_Distribution.objects.get(mineral_name = mineral,subgrid_id = s)
        temp.append(l.mineral_name)
        temp.append(l.mineral_quantity)
        if(l.mineral_quantity > 0):
            l.mineral_quantity = l.mineral_quantity -1
        temp.append(l.mineral_quantity)
        l.save()
    return temp
    
"""def rovermovement(request):
    k = Grid.objects.create(grid_sizex = 10,grid_sizey = 12)
    k.save()
    addminerals(k)
    if request.method == "POST":
        positionx = request.POST['positionx']
        positiony = request.POST['positiony']
        direction = request.POST['direction']
        movement = request.POST['movement']
        post = Rover.objects.create(rover_initposx = positionx, rover_initposy = positiony, rover_initdirection = direction, rover_movement = movement)
        post.save()
        get_final_movement(post)
        return HttpResponseRedirect('/result')

    else:
        return render_to_response('front.html',context_instance = RequestContext(request))
    return render_to_response('front.html')
"""
def roverdisplay(request):
    
    if request.method == "POST":
        form = Roverform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            x = roverworking(cd['rover_initposx'], cd['rover_initposy'], cd['rover_initdirection'], cd['rover_movement'], cd['rover_sense'], cd['rovergrid_id'])
            return HttpResponse(x)
        else:
            return render_to_response('frontform.html',{'form':form},context_instance = RequestContext(request))
    else:
        form = Roverform()
        return render_to_response('frontform.html',{'form':form},context_instance = RequestContext(request))

def check(request):
    s = Subgrid.objects.filter(subgrid_posx = 2, subgrid_posy = 1)
    l = Mineral_Distribution.objects.filter(mineral_name = "gold",subgrid_id = s)
   # l.mineral_quantity = l.mineral_quantity-1
    for i in l:
        i.mineral_quantity = i.mineral_quantity -1
    
    return render_to_response("frontform.html",{"l":l}, context_instance = RequestContext(request))

def cleardata(request):
    Mineral_Distribution.objects.all().delete()
    Subgrid.objects.all().delete()
    return HttpResponse("frontform.html")
    
    
        