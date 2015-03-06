from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import tinyble
from tinyble import where

# Create your views here.
db = tinyble.Tinyble('db').collection('example')

def home(request):

	if request.method == 'POST':

		if 'add' in request.POST:
			db.insert({'content':request.POST['content']})
			return redirect(reverse('home'))
		elif 'delete' in request.POST:
			db.remove(eids=[int(request.POST['content'])])

	content = db.get(eid=3)

	return render(request, 'home.html', {'content': content})
