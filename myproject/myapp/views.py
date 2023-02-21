from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse

def home_html(request):
    return render(request, 'cv.html')


def contact_us_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print('email:', form.cleaned_data['email'])
            print('message:', form.cleaned_data['message'])
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    
    return render(request, "contact.html", {'form':form})
