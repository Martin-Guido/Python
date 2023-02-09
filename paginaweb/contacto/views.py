from django.shortcuts import render, redirect
from .forms import formulariocontacto
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def contacto(request):
	formulario_contacto=formulariocontacto()
	if request.method=='POST':
		formulario_contacto=formulariocontacto(data=request.POST)
		if formulario_contacto.is_valid():
		#	inffor=formulario_contacto.cleaned_data
			nombre=request.POST.get('nombre')
			email=request.POST.get('email')
			mensaje=request.POST.get('mensaje')
	
			
			mail=EmailMessage("Mensaje desde pagina web",
				"EL usario con nombre {} con la direccion {} escribe lo siguiente: \n \n{}".format(nombre,email,mensaje),
				"",["***@gmail.com"],reply_to=[email])
			try :
				mail.send()
				return redirect('/contacto/?valido')
			except:
				return redirect('/contacto/?invalid')
			
	return  render(request,'contacto/contacto.html',{'miformulario':formulario_contacto})
# Create your views here.
