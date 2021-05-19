from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import ContactUs
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("HOMEPAGE")
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('text')
        contact = ContactUs(name=name, email=email, query=query, date=datetime.today())
        contact.save()
        messages.success(request, 'Query has been submitted. Kindly check your email for updates')
    return render(request, 'contact.html')
