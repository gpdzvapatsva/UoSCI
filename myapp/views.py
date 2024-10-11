from django.shortcuts import render

from myapp.models import Students


# Create your views here.
def index(request):
    return render (request, 'index.html')
def records(request):
    students=Students
    context={'students':students}
    return render (request, 'records.html')
def contact(request):
    return render(request, template_name='contact.html')
