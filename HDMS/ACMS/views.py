from django.shortcuts import render
from .forms import LoginForm, PatientForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import hashers
from models import hmo_list, state


# Create your views here.

def index(request):
    if request.method == "POST": # checking if it's a post request
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                if user.is_active: # checking if the user is still active
                    login(request, user) # logging the user in
                    request.session.set_expiry(1800) # setting the session expiry time, after which login is required
                    return HttpResponseRedirect(reverse('ACMS:homepage'))

            else:
                try:
                    username = User.objects.get(username = form.cleaned_data["username"])
                    # since authenticate method returns none for inactive registered users, the if statement below takes care of checking if user exist
                    # but inactive in order to forward the right feedback message
                    if username and hashers.check_password(form.cleaned_data["password"], User.objects.get(username = username).password):
                        messages.error(request, "Your account has been disabled! Contact Admin...")
                        return HttpResponseRedirect(reverse('ACMS:index'))
                    else:
                         messages.error(request, 'Incorrect username and password!!!') # saving message error to be displayed on template
                         return HttpResponseRedirect(reverse('ACMS:index'))
                except:
                    messages.error(request, 'Incorrect username and password!!!') # saving message error to be displayed on template
                    return HttpResponseRedirect(reverse('ACMS:index'))

# if the request is a GET request
    else:
        form = LoginForm() # creating new form
        if request.path == "/acms/login/":
            messages.info(request, "Please log in");
        logout(request) # logging out the user and clearing the user's session

    return render(request, 'acms/index.html', {"form": form})



@login_required(redirect_field_name="", login_url='/acms/login') # login required to view this page
def homepage(request):
    admin = False
    if request.user.is_staff: admin = True # checking if the user has administrative rights
    context = {"name" : "%s %s" % ( request.user.first_name, request.user.last_name), "username" : request.user.username, "admin" : admin} # declaring the template context
    return render(request, 'acms/homepage.html', context) # rendering the homepage template

@login_required(redirect_field_name="", login_url='/acms/login')
def workpage(request):
    admin = False
    if request.user.is_staff: admin = True
    patient_form = PatientForm(auto_id= False)
    context = {"name" : "%s %s" % (request.user.last_name, request.user.first_name), "username" : request.user.username, 'admin': admin, "patient_form" : patient_form}
    return render(request, 'acms/workpage.html', context)







