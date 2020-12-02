from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.utils import timezone


# Create your views here.

def contact(request):
    name, email, web, message = None, None, None, None
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        web = request.POST.get('web')
        message = request.POST.get('message')
        print(name, email, web, message)
        Contact.objects.create(username=name, email=email, site=web, message=message, create=timezone.now())

    context = {
        "messages": Contact.objects.all().values('username', 'message')
    }
    return render(request, 'contact/index.html', context)
