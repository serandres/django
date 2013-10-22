from random import choice
frases = ['python manage','django framework','node js']

def ejemplo(request):
	return {'frase': choice(frases)}

from django.core.urlresolvers import reverse

def menu(request):
	menu = {'menu': [
		{'name': 'Home', 'url': reverse('home')},
		{'name': 'Add', 'url': reverse('add')},
	]}
	for item in menu['menu']:
		if request.path == item['url']:
			item['active'] = True
	return menu   