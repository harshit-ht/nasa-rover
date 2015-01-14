from django.shortcuts import render, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from register.loginform import userform, Registerform

def register_member(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')

    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            user = User.objects.create(username = form.cleaned_data['email'], email = form.cleaned_data['email'], password = form.cleaned_data['password2'])
            user.set_password(form.cleaned_data['password2'])
            user.save()
            return HttpResponseRedirect('/profile')

        else:
            return render_to_response('register.html',{'form':form}, context_instance = RequestContext(request))

    else:
        form = Registerform()
        return render_to_response('register.html',{'form':form},context_instance = RequestContext(request))


def login_member(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if request.method == "POST":
        form = userform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            member = authenticate(username = username, password = password)
            if member is not None:
                login(request, member)
                return HttpResponseRedirect('/profile')
            else:
                return render_to_response('login.html',{'form':form}, context_instance = RequestContext(request))
        else:
            return render_to_response('login.html', {'form':form}, context_instance = RequestContext(request))
            
    else:
        form = userform()
        return render_to_response('login.html', {'form':form}, context_instance = RequestContext(request))
    
def logout_member(request):
    logout(request)
    return HttpResponseRedirect("/login")

def profile(request):
    return render_to_response('profile.html',context_instance = RequestContext(request))
        

# Create your views here.
