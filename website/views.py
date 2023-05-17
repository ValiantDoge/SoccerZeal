from django.shortcuts import render
from website.forms import *

# Create your views here.

def index(request):
    context = {
        'nbar': 'home'
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'nbar': 'about'
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        print("Post form")
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
            'name': form.cleaned_data['name'],
            'subject': form.cleaned_data['subject'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message'],
            }
            
            email_header = "A new client is trying to contact you:"
            # message = "\n".join([email_header] + [f"{key}: {value}" for key, value in body.items()])
            # response = "Your message has been sent. Thank you!"

            #Email to User
            subject = "Received Inquiry"
            message = f"Hi {body.get('name')}, we have received your email. We'll get back to you shortly."
            email = body.get('email')

            #Email to Comapny
            subject_company = f"(Website Inquiry) "+body.get('subject')
            message_company = "\n".join([email_header] + [f"Name:\n{body.get('name')} \n\nMessage: \n{body.get('message')}"])
            

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER,[email])

                #Email to Company
                send_mail(subject_company, message_company, email,[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return redirect('contact')
        else:
            print(form.errors)
      
    form = ContactForm()
    context = {
        'form':form,
        'nbar': 'contact',
    }
    return render(request, "contact.html", context)
    
  

def achivements(request):
    context = {
        'nbar': 'achivement'
    }
    return render(request, 'achivement_details.html', context)

def blog(request):
    context = {
        'nbar': 'blog'
    }
    return render(request, 'blog.html', context)

def blogDetails(request):
    context = {
        'nbar': 'blogDetails'
    }
    return render(request, 'blogDetails.html', context)

def clubHistory(request):
    context = {
        'nbar': 'clubHistory'
    }
    return render(request, 'clubHistory.html', context)

def gallery(request):
    context={
        'nbar': 'gallery'
    }
    return render(request, 'gallery02.html', context)

def playerDetails(request):
    context={
        'nbar': 'playerDetails'
    }
    return render(request, 'playerDetails.html', context)

def user_login(request):
    context={
        'nbar': 'login'
    }
    return render(request, 'login.html', context)

def user_register(request):
    context={
        'nbar': 'register'
    }
    return render(request, 'register.html', context)



