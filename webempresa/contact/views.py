from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Suponiendo que todo ha ido bien
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                #asunto,
                "La Caffettiera: Nuevo mensaje de contacto",
                #cuerpo,
                "De {}<{}>\n\nEscribió:\n\n{}".format(name, email, content),
                #email_origen,
                "no-contestar@inbox.mailtrap.io",
                #email_destino,
                ["ambientalgoloka@gmail.com"],
                #email responder
                reply_to=[email]
            )
            try:
                email.send()
                # todo ha ido bien
                return redirect(reverse('contact') + "?ok")
            except:
                # algo no ha ido bien, se redirecciona a fail
                return redirect(reverse('contact') + "?fail")    

    return render(request,"contact/contact.html",{'form':contact_form})