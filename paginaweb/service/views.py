from django.shortcuts import render
from service.models import service as s
# Create your views here.
def service(request):

	servicios=s.objects.all()
	return  render(request,'service/service.html',{'servicios':servicios})
