from django.shortcuts import (
    render,
    redirect,
    HttpResponseRedirect,
    get_object_or_404,
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
    RegisterUserForm,
    ProfileForm
)
from accounts.forms import SendMessageForm
from .models import Profile
from articles.models import Article
# Create your views here.
latest_articles = Article.objects.all()[0:3]
# Contact Us View:
def contact_us(request):
    # send message Form Validations:
    send_message_form=SendMessageForm()
    if request.method == "POST":
        send_message_form = SendMessageForm(request.POST)
        if send_message_form.is_valid():
            send_message_form.save()
            return redirect('articles:articles')
    # Context:
    context = {
        'send_message_form':send_message_form,
        'latest_articles':latest_articles,
    }
    # Template:
    return render(request, 'accounts/contact.html', context)

# User Profile View:
def profile(request):
    if request.user.is_authenticated:
        # QuerSet:
        user_info = Profile.objects.get(user=request.user)
        # Profile Form Validations:
        profile_form = ProfileForm(instance=user_info)
        if request.method == "POST":
            profile_form = ProfileForm(request.POST, request.FILES, instance=user_info)
            if profile_form.is_valid():
                insert = profile_form.save(commit=False)
                insert.save()
                return HttpResponseRedirect('.')
            else:
                return HttpResponseRedirect('.')
        # Profile Form Validations:
        # Context
        context = {
            'profile_form':profile_form,
            'user_info':user_info,
            'latest_articles':latest_articles,
        }
        # Template:
        return render(request, 'accounts/profile.html', context)
    else:
        return redirect('accounts:login')

# User register View:
def register_user(request):
    if not request.user.is_authenticated:
        # User Register form validations:
        user_register_form = RegisterUserForm()
        if request.method == "POST":
            user_register_form = RegisterUserForm(request.POST or None)
            if user_register_form.is_valid():
                user_register_form.save()
                return redirect('accounts:login')
            else:
                user_register_form = RegisterUserForm(request.POST or None)
                
        context = {
            "user_register_form":user_register_form,
        }
        # templates:
        return render(request, 'accounts/register.html', context)
    else:
        return redirect('home')


# user login View:
def login_user(request):
    if not request.user.is_authenticated:
        # User Login Form validations:
        user_login_form = LoginUserForm()
        if request.method == "POST":
            user_login_form = LoginUserForm(request.POST or None)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:profile')
            else:
                messages.warning(request, 'please enter a valid informatins')
        # Template:
        template = loader.get_template('accounts/login.html')
        # Context:
        context = {
            "user_login_form":user_login_form,
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