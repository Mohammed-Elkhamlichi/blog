from django.shortcuts import (
    render,
    redirect,
    HttpResponseRedirect
)
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from .forms import (
    LoginUserForm,
    RegisterUserForm
)
# Create your views here.

# User Profile View:
def profile(request, username):

    # QuerSet:
    # user = User
    # Context
    context = {}
    # Template:
    return render(request, 'accounts/profile.html', context)

# User register View:
def register_user(request):
    if not request.user.is_authenticated:
        # form validations:
        form = RegisterUserForm()
        if request.method == "POST":
            form = RegisterUserForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('accounts:login')
            else:
                form = RegisterUserForm(request.POST or None)
                
        context = {
            "form":form,
        }
        # templates:
        return render(request, 'accounts/register.html', context)
    else:
        return redirect('home')


# user login View:
def login_user(request):
    if not request.user.is_authenticated:
        # form validations:
        form = LoginUserForm()
        if request.method == "POST":
            form = LoginUserForm(request.POST or None)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'please enter a valid informatins')
        # template:
        template = loader.get_template('accounts/login.html')
        context = {
            "form":form,
        }
        return HttpResponse(template.render(context, request))
        # or
        # return render(request, 'accounts/login.html', context)
    else:
        return redirect('home')


# user logout view:
@login_required
def logout_user(request):
    logout(request)
    return redirect('accounts:login')