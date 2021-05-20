from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Testimonial,Photo,Course,Website_title,Services
from django.views.generic import DetailView,FormView
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic.edit import CreateView
from .forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin

def home(request):
    context = {
        'members':Testimonial.objects.all(),
        'photos' : Photo.objects.all(),
        'tags': Website_title.objects.all(),
        'services':Services.objects.all()
        

        }
    return render(request,'index.html',context)

def Course_View(request):
    context = {
            "topics" : Course.objects.all()
        }
    return render(request,'course.html',context)        

class Course_Detail(DetailView):
    model = Course
    template_name = "detail.html"


class ContactFormView(SuccessMessageMixin,FormView):

    form_class = ContactForm
    template_name = 'index.html'
    success_url = '/sucess/'
    success_message = "Thank You For Connecting Us"

    def form_valid(self,form):
        message = "Name={name}\nEmail={email}\nSubject={subject}\nsaid: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'),
            subject = form.cleaned_data.get('subject'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email='englishhubsolutions@gmail.com',
            recipient_list=['hirenmukherjee@gmail.com'],
        )
        form.save()
        return super().form_valid("thank you for connecting us")
