from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Etudiant
from .forms import EtudiantForm
from django.http import  HttpResponseRedirect

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def students_list(request):
    students = Etudiant.objects.all().order_by('nom')
    return render(request, 'students/students_list.html', {'students': students,})

def add_student(request):
      submitted = False
      if request.method == "POST":
            form = EtudiantForm(request.POST)
            if form.is_valid():
                  form.save()
            return HttpResponseRedirect('/add_student?submitted=True')
      else:
            form = EtudiantForm
      if 'submitted' in request.GET:
            submitted=True
      return render(request, 'students/add_student.html', {
        'form': form,
        'submitted': submitted,
        })