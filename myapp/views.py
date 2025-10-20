"""
myapp.views
------------
Simple Django views for the myapp application.

Views:
- index: Render the homepage.
- records: Query all Students and render the records template with context.
- contacts: Render the contact form page.

References:
- Model: [`myapp.models.Students`](myapp/models.py)
- Templates:
  - [myapp/templates/index.html](myapp/templates/index.html)
  - [myapp/templates/records.html](myapp/templates/records.html)
  - [myapp/templates/contacts.html](myapp/templates/contacts.html)
- URL config: [myapp/urls.py](myapp/urls.py)
"""
from typing import Dict
from django.shortcuts import render

from .models import Students

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Render the homepage.

    Template: 'index.html'
    Context: None
    """
    return render(request, 'index.html')


def records(request: HttpRequest) -> HttpResponse:
    """
    Fetch all Students and render the records page.

    Template: 'records.html'
    Context:
        - 'students': QuerySet of [`myapp.models.Students`](myapp/models.py)

    Example:
        In the template iterate as:
            {% for student in students %}
              {{ student }}
            {% endfor %}
    """
    students = Students.objects.all()
    context: Dict[str, object] = {'students': students}
    return render(request, 'records.html', context)


def contacts(request: HttpRequest) -> HttpResponse:
    """
    Render the contact form page.

    Template: 'contacts.html'
    Context: None
    """
    return render(request, 'contacts.html')

