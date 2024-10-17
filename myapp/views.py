from django.shortcuts import render

from .models import Students


# Create your views here.
def index(request):
    return render (request, 'index.html')
def records(request):
    students=Students.objects.all()
    context={'students':students}
    return render (request, 'records.html', context)
def contacts(request):
    return render (request, 'contacts.html')

