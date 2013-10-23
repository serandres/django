from django.shortcuts import redirect
from random import choice

paises = ['Colombia', 'Peru', 'Panama', 'Mexico']

def de_donde_vengo(request):
	return choice(paises)

class PaisMiddleWare():
	def process_request(self,request):
		pais = de_donde_vengo(request)
		if pais == 'Otrro':
			return redirect('http://mejorando.la')